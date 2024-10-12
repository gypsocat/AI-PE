function sendData() {
    // 获取输入框的值
    var name = document.getElementById("name").value;
    var ID = document.getElementById("ID").value;
    var sex = document.getElementById("sex").value;
    var birthday = document.getElementById("birthday").value;
    
    // 创建XMLHttpRequest对象
    var xhr = new XMLHttpRequest();
  
    // 设置请求方法和URL
    xhr.open("POST", "https://gypsocat.com/  ", true);
  船都
    // 设置请求头
    xhr.setRequestHeader("Content-Type", "application/json");
  
    // 构建要发送的数据对象
    var data = {
      name: name,
      ID: ID,
      sex: sex,
      birthday:birthday,
    };
  
    // 将数据对象转换为JSON字符串
    var jsonData = JSON.stringify(data);
  
    // 监听请求状态变化
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // 请求成功
        console.log(xhr.responseText);
      }
    };
  
    // 发送请求
    xhr.send(jsonData);
  }
