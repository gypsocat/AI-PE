//=====================================保存视频文件=======================================
let start = false;
let load = false;
let spendtime = 0;
let updateDataEnabled = true; // 添加一个变量来控制是否执行 updateData()

function updateData() {
    if (!updateDataEnabled) return; // 如果 updateDataEnabled 为 false，则不执行后续代码

    // 其余代码不变
}

// 在重置按钮的事件处理程序中将 updateDataEnabled 设置为 false
document.getElementById('resetButton').addEventListener('click', () => {
    // 停止录制等操作...
    updateDataEnabled = false; // 设置 updateDataEnabled 为 false，停止 updateData() 的执行
});



function updateData() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_suggestion', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                // 更新计数
                var countElement = document.getElementById('count');
                countElement.innerText = response.sportNum;

                // 更新建议
                var suggestionElement = document.getElementById('suggestion');
                suggestionElement.innerText = response.suggestion[response.suggestion.length - 1];


                console.log("===================================================");
                console.log(response);
            } else {
                // 处理错误情况
                console.error('Request failed with status:', xhr.status);
            }
        }
    };
    xhr.send(); 
}

document.addEventListener('DOMContentLoaded', () => {
    let mediaRecorder;

    async function startRecording() {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        mediaRecorder = new MediaRecorder(stream);
        console.log(mediaRecorder);

        var resetXhr = new XMLHttpRequest();
        resetXhr.open('GET', '/reset_file_content');
        resetXhr.send();


        mediaRecorder.ondataavailable = async (event) => {
            if (event.data && event.data.size > 0) {
                const formData = new FormData();
                formData.append('video', event.data, 'upanddown.mp4');
    
                await fetch('/upload_video1', {
                    method: 'POST',
                    body: formData
                });
                await fetch('/upload_video2', {
                    method: 'POST',
                    body: formData
                });
            }
        };
    
        mediaRecorder.start();
    }

    function stopRecording() {
        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
            mediaRecorder.stop();
        }
    }

    // 开始录制按钮
    document.getElementById('startButton').addEventListener('click', () => {
        if (mediaRecorder && mediaRecorder.state === 'paused') {
            mediaRecorder.resume();
        } else {
            startRecording();
            const xhr1 = new XMLHttpRequest();
            xhr1.open('GET', '/run_learn1');
            console.log("try to open learn1");
            xhr1.send();
        }
        start = true;
        load = false;
        //===============================================
        updateInterval = setInterval(updateData, 500); // 每秒更新数据
    });
    

    // 暂停录制按钮
    document.getElementById('pauseButton').addEventListener('click', () => {
        if (mediaRecorder && mediaRecorder.state === 'recording') {
            mediaRecorder.pause();
        }
        start = false;
        //console.log("start:"+start);
    });

    // 停止录制按钮
    document.getElementById('resetButton').addEventListener('click', () => {
        stopRecording();
        const xhr = new XMLHttpRequest();
        xhr.open('GET', '/run_interaction');
        console.log("try to open interaction");
        xhr.send();
        console.log("send interaction success");
        start = false;
        console.log("start:"+start);
        var xhr2 = new XMLHttpRequest();
        xhr2.open('GET', '/run_conclusion');
        var data = {
            time: spendtime,
        }
        xhr2.send(JSON.stringify(data));
        // 停止更新数据
        clearInterval(updateInterval);
        // 重置 suggestion 和 sportNum
        updateDataEnabled = false;


        document.getElementById('suggestion').innerText = "无";
        document.getElementById('count').innerText = "0";


        var xhr1 = new XMLHttpRequest();
        xhr1.open('POST', '/reset_data', true);
        xhr1.setRequestHeader('Content-Type', 'application/json');
        xhr1.onreadystatechange = function() {
            if (xhr1.readyState === XMLHttpRequest.DONE) {
                if (xhr1.status === 200) {
                    console.log('Data reset successfully');
                } else {
                    console.error('Failed to reset data:', xhr1.status);
                }
            }
        };
        xhr1.send();

    });

});

//============================================保存视频文件==============================================

//==============================================上传视频===============================================

function uploadVideo() {
    // 创建一个input元素
    var input = document.createElement('input');
    input.type = 'file';
    input.accept = 'video/*';
    // 添加change事件监听器
    input.addEventListener('change', async function () {
        var file = input.files[0];
        var uniqueId = Date.now(); // 生成一个唯一编号
        var newFileName = 'video/' + uniqueId + '.mp4'; // 构建新的文件名
        const formData = new FormData();
        formData.append('video', file, newFileName);
        try {
            const response1 = await fetch('/upload_video1', {
                method: 'POST',
                body: formData
            });
            const result1 = await response1.json();
            console.log(result1);

            const response2 = await fetch('/upload_video2', {
                method: 'POST',
                body: formData
            });
            const result2 = await response2.json();
            console.log(result2);
        } catch (error) {
            console.error('上传失败：', error);
        }
    });
    // 触发input元素的点击事件
    input.click();
}
//==============================================上传视频===============================================


//=========================================获取视频的图像数据============================================

function setupCamera() {
    return navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            const video = document.createElement('video');
            video.srcObject = stream;
            video.setAttribute('autoplay', '');
            video.setAttribute('playsinline', '');
            return new Promise(resolve => {
                video.addEventListener('loadedmetadata', () => {
                    const canvas = document.getElementById('canvas');
                    const ctx = canvas.getContext('2d');
                    canvas.getContext('2d').willReadFrequently = true; // 设置willReadFrequently属性为true
                    canvas.width = video.videoWidth;
                    canvas.height = video.videoHeight;
                    resolve({ video, canvas, ctx });
                });
            });
        });
}

setupCamera()
    .then(({ video, canvas, ctx }) => {
        video.play();
        drawFrame(video, canvas, ctx);
    })
    .catch(error => {
        console.log("获取摄像头失败:", error);
    });


    let lastSendTime = 0;
    const sendInterval = 100; // 设置发送间隔为1秒


    
function drawFrame(video, canvas, ctx) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.scale(-1, 1); // 水平镜像翻转
    ctx.drawImage(video, -canvas.width, 0, canvas.width, canvas.height); // 绘制图像
    ctx.restore();

        if(start && timeLeft != 0){
        const currentTime = Date.now();
        if (currentTime - lastSendTime >= sendInterval) {
//============================遍历每个像素的数据，并将其以 RGBA 格式打印出来========================================
// var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
// var pixelData = imageData.data;

// for (var i = 0; i < pixelData.length; i += 4) {
//     var red = pixelData[i];
//     var green = pixelData[i + 1];
//     var blue = pixelData[i + 2];
//     var alpha = pixelData[i + 3];

//     console.log("Pixel at position " + i / 4 + " is: RGBA(" + red + ", " + green + ", " + blue + ", " + alpha + ")");
// }
//=============================================================================================================
        sendImageData(ctx.getImageData(0, 0, canvas.width, canvas.height)); // 将图像数据发送到后端
        lastSendTime = currentTime; // 更新上次发送时间
        }
      }
    requestAnimationFrame(() => drawFrame(video, canvas, ctx));
}
// 初次调用
requestAnimationFrame(() => drawFrame(video, canvas, ctx));

function sendImageData(imageData) {
    // 将图像数据发送到Flask服务器
    fetch('/realtime_upload', {
        method: 'POST',
        body: imageData.data
    })
    .then(response => {
        if (response.ok) {
            console.log('Video frame data sent successfully');
        } else {
            console.error('Failed to send video frame data');
        }
    })
    .catch(error => {
        console.error('Error sending video frame data:', error);
    });
}


//=======================================================================================================



//======================================倒计时================================
//有一个BUG:如果连续按多次“开始”按钮，那么倒计时会变得很快（应该是按几次加速几倍）
//然后按“暂停”只能降低一倍速度，按“重置”完全没用（这两个按钮按几次都是一样的效果）
//===========================================================================
let timerInterval;
let timeLeft = 60; // 1 minutes in seconds


const startButton = document.getElementById('startButton');
const pauseButton = document.getElementById('pauseButton');
const resetButton = document.getElementById('resetButton');
// const timerSpan = document.getElementById('timer');
if (document.location.pathname === '/student_video_mobile') {
    console.log("1111111111111111111111111");
     timerSpan = document.getElementById('timer'); // index.html中的计时器元素ID为timer
} else if (document.location.pathname === '/student_video_mobile_fullscreen') {
     timerSpan = document.getElementById('timer1'); // other.html中的计时器元素ID为timer1
} else {
    // 如果路径不匹配任何已知的页面，则设置一个默认值
     timerSpan = document.getElementById('timer');
}

function updateTimer() {
    
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    timerSpan.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    if (timeLeft === 10) {
      timerSpan.style.color = 'red'; // Change color to red when 10 seconds left
  }
    if (timeLeft === 0) {
        clearInterval(timerInterval);
    } else {
        timeLeft--;
        spendtime++;
    }
}

startButton.addEventListener('click', async() => {
    timerInterval = setInterval(updateTimer, 1000);
});

pauseButton.addEventListener('click', () => {
    clearInterval(timerInterval);
});

resetButton.addEventListener('click', () => {
    clearInterval(timerInterval);
    timeLeft = 60;
    updateTimer();
    if (timerSpan.id === 'timer') {
        timerSpan.style.color = 'black'; // 设置为黑色
    } else if (timerSpan.id === 'timer1') {
        timerSpan.style.color = 'white'; // 设置为白色
    }
});

//按下按钮变色
function startButtonClicked() {
  document.getElementById('pauseButton').classList.add('btn-primary');
  document.getElementById('pauseButton').classList.remove('btn-danger');
  document.getElementById('startButton').classList.remove('btn-primary');
  document.getElementById('startButton').classList.add('btn-info');
}

function pauseButtonClicked() {
  document.getElementById('pauseButton').classList.remove('btn-primary');
  document.getElementById('pauseButton').classList.add('btn-danger');
  document.getElementById('startButton').classList.remove('btn-info');
  document.getElementById('startButton').classList.add('btn-primary');
}

function resetButtonClicked() {
  document.getElementById('startButton').classList.remove('btn-info');
  document.getElementById('startButton').classList.add('btn-primary');
  document.getElementById('pauseButton').classList.remove('btn-danger');
  document.getElementById('pauseButton').classList.add('btn-primary');
  document.getElementById('resetButton').classList.add('btn-danger');
  timerSpan.style.color = 'black'; // Reset color to default
  setTimeout(() => {
      document.getElementById('resetButton').classList.remove('btn-danger');
      document.getElementById('resetButton').classList.add('btn-primary');
  }, 1000);
}


//这个部分似乎还有点小BUG，可能会直接在前端展示向大模型输入的部分
function generateButtonClicked() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_file_content');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var markdownText = xhr.responseText;
            console.log("mark:"+typeof marked)
            console.log(marked);
            var htmlText = marked.marked(markdownText);
            console.log(htmlText);
            document.getElementById('evaluation').innerHTML = htmlText;
            
            // Check if responseText is "加载中......"
            if (markdownText.trim() === '加载中......' && load) {
                // If it is, continue checking every second
                setTimeout(generateButtonClicked, 1000);
            } else {
                // If not, send request to change file content to "加载中......"
                var getXhr = new XMLHttpRequest();
                getXhr.open('GET', '/get_file_content');
                getXhr.send();
            }
            
        }
    };
    xhr.send();
    load = true;
}

function generateButtonClicked_comment() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_file_content_comment');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var markdownText = xhr.responseText;
            console.log("mark:"+typeof marked)
            console.log(marked);
            var htmlText = marked.marked(markdownText);
            console.log(htmlText);
            document.getElementById('comment').innerHTML = htmlText;
            
            // Check if responseText is "加载中......"
            if (markdownText.trim() === '加载中......' && load) {
                // If it is, continue checking every second
                setTimeout(generateButtonClicked, 1000);
            } else {
                // If not, send request to change file content to "加载中......"
                var getXhr = new XMLHttpRequest();
                getXhr.open('GET', '/get_file_content_comment');
                getXhr.send();
            }
            
        }
    };
    xhr.send();
    load = true;
}

//document.getElementById('generateButton').addEventListener('click', generateButtonClicked);
