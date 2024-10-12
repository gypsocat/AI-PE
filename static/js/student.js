function openModal(detail, sport_type,time) {

     // 创建一个对象，包含 detail 和 time 字段
     var data = {
      'detail': detail,
      'sport_type':sport_type,
      'time': time
  };
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/get_details", true);
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      // 检查响应状态
      if (xhr.status === 200) {
        // 处理响应数据
        var data = JSON.parse(xhr.responseText);
        console.log("data:",data);
      } else {
        // 处理错误
        console.error('There was a problem with your XHR request:', xhr.statusText);
      }
    }
  };

  xhr.onerror = function() {
    // 处理错误
    console.error('There was a problem with your XHR request.');
  };
  // 发送请求
  xhr.send(JSON.stringify({data}));
 

    // console.log(sportType);
    // console.log(score);
    // console.log(time);
    // // 将信息填充到模态框中
    // document.getElementById('sportType').innerText = '运动类型：' + sportType;
    // document.getElementById('score').innerText = '运动得分：' + score;
    // document.getElementById('time').innerText = '时间：' + time;
  // 获取模态框元素
  var modalElement = document.getElementById('details_modal');
  // 创建 Bootstrap 模态框对象
  var modal = new bootstrap.Modal(modalElement);
  // 显示模态框
  modal.show();
}

let progressValue = parseInt("{{progress}}");



// 监听按钮的点击事件
document.querySelectorAll('.dropdown-toggle').forEach(button => {
  button.addEventListener('click', function() {
    // 获取与按钮关联的下拉菜单
    const dropdownMenu = this.nextElementSibling;
    
    // 检查下拉菜单的展开状态，并输出到控制台
    if (dropdownMenu.classList.contains('show')) {
      console.log('下拉菜单已关闭');
    } else {
      console.log('下拉菜单已打开');
      // 打印下拉菜单中的内容
      const dropdownHeader = dropdownMenu.querySelector('.dropdown-header');
      if (dropdownHeader) {
        console.log('下拉菜单内容:', dropdownHeader.innerText);
      }
    }
  });
});
