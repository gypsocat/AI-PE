// // 创建WebSocket连接
// const socket = new WebSocket('ws://your-chatgpt-server-url');

// // 监听WebSocket连接事件
// socket.onopen = function(event) {
//   console.log('WebSocket connection established.');
// };

// // 监听WebSocket消息事件
// socket.onmessage = function(event) {
//   const message = event.data;
//   displayMessage(message);
// };

// // 发送消息给chatGPT
// function sendMessage(message) {
//   socket.send(message);
// }

// 显示聊天消息
function display_my_message(message) {
  const messageContainer = document.getElementById('chat-container');
  //console.log(messageContainer);

  const messageElement = document.createElement('div');
  messageElement.setAttribute('class','d-flex justify-content-end align-items-center text-right');

  const info = document.createElement('div');
  info.setAttribute('class','pr-2');

  const name = document.createElement('span');
  name.setAttribute('class','name');
  name.textContent = '用户名（还没链接好）';
  const msg = document.createElement('p');
  msg.setAttribute('class','msg');
  msg.textContent = message;

  info.appendChild(name);
  info.appendChild(msg);

  const img_container = document.createElement('div');
  const user_img = document.createElement('img');
  user_img.setAttribute('class','img1');
  user_img.setAttribute('src','avatars/avatar1.jpeg');
  user_img.setAttribute('width','30');

  img_container.appendChild(user_img);

  messageElement.appendChild(info);
  messageElement.appendChild(img_container);

  messageContainer.appendChild(messageElement);
  const scrollContainer = document.getElementById('chat-container');
  scrollContainer.scrollTop = scrollContainer.scrollHeight;
  //console.log(scrollContainer.scrollHeight);
}


//发送信息
function submitMessage() {
      const inputBox = document.getElementById('text-input');
      const message = inputBox.value;
      //console.log(message);
     //sendMessage(message);
      inputBox.value = ''; // 清空输入框
      display_my_message(message);
  }

//回车发送信息
  const button = document.getElementById('submit-que');
  document.addEventListener('keydown', function(event){
    if(event.key === 'Enter'){
      submitMessage();
    }
  });


