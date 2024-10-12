function sendData(name, ID) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://gypsocat.com/profile', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({name: name, ID: ID}));
    console.log('POST');
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log('Data sent successfully');
        }
    };
}

function getData() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://gypsocat.com/profile_getdata', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send();
    console.log('GET！！！！！！！');
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log('data呢');
            var data = JSON.parse(xhr.responseText);
            console.log('xhr.responseText'+data);
            console.log(data.name);
            console.log(data.ID);
            document.getElementById('email').setAttribute('placeholder', data.name);
            document.getElementById('last_name').setAttribute('placeholder', data.ID);
        }
    };
}

document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('set_user_settings');
    button.addEventListener('click', function(event) {
        event.preventDefault();
        var name = document.getElementById('name').value;
        var ID = document.getElementById('ID').value;
        sendData(name, ID);
        console.log('sendData OK');
        //仅用来测试
        getData();
        console.log('getData OK');
    });
    //这里的getData() 函数是在页面加载完成后立即执行的，之后用得到！！！！！！！！！！！！！！！
    // getData();
    // console.log('getData OK');
});


document.getElementById("set_user_settings").addEventListener("click", function(event) {
    event.preventDefault();
    var modal = new bootstrap.Modal(document.getElementById('modal-1'));
    modal.show();
    setTimeout(function() {
        modal.hide();
    }, 1500);
});

