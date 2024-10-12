<script src="utils.js"></script>


function renderChatMessage(message) {
  const container = document.getElementById("chat-message-item");

  const messageDiv = document.createElement("div");
  messageDiv.classList.add("chat-message-item");

  const markdownContent = getMessageTextContent(message);
  const markdownElement = document.createElement("div");
  markdownElement.textContent = markdownContent;

  messageDiv.appendChild(markdownElement);

  const images = getMessageImages(message);
  if (images.length === 1) {
      const img = document.createElement("img");
      img.classList.add("chat-message-item-image");
      img.src = images[0];
      img.alt = "";
      messageDiv.appendChild(img);
  } else if (images.length > 1) {
      const imagesDiv = document.createElement("div");
      imagesDiv.classList.add("chat-message-item-images");
      imagesDiv.style.setProperty("--image-count", images.length);

      images.forEach((image, index) => {
          const img = document.createElement("img");
          img.classList.add("chat-message-item-image-multi");
          img.src = image;
          img.alt = "";
          imagesDiv.appendChild(img);
      });

      messageDiv.appendChild(imagesDiv);
  }

  container.appendChild(messageDiv);
}

// 示例消息对象
const message = {
  content: "Hello, World!",
  images: ["image1.jpg", "image2.jpg"]
};

// 渲染消息
renderChatMessage(message);





// class FrontendClientApi {
//     constructor() {
//       this.llm = new GeminiProApi(); // 创建 GeminiProAPI 实例
//     }
  
//     async getResponse(message) {
//       // 发送请求到后端获取聊天模型的回答
//       const response = await fetch('/your-backend-endpoint', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//           message: message
//         })
//       });
  
//       // 解析后端返回的数据
//       const data = await response.json();
  
//       // 返回聊天模型的回答
//       return data.response;
//     }
//   }
  
//   // 创建 FrontendClientApi 实例
//   const frontendClientApi = new FrontendClientApi();
  
//   // 示例：发送消息并显示回答
//   const sendMessageButton = document.getElementById('send-message-button');
//   const messageInput = document.getElementById('message-input');
//   const responseContainer = document.getElementById('response-container');
  
//   sendMessageButton.addEventListener('click', async () => {
//     const message = messageInput.value;
//     const response = await frontendClientApi.getResponse(message);
//     responseContainer.innerHTML = response;
//   });
  