document.addEventListener("DOMContentLoaded", function() {
    // 存储已点击项的数组
    let clickedItems = [];

    // 获取所有的 list-group-item 元素
    const listItems = document.querySelectorAll('.list-group-item');

    // 遍历所有的 list-group-item 元素
    listItems.forEach(item => {
        // 为每个 list-group-item 添加点击事件监听器
        item.addEventListener('click', function() {
            // 获取任务详情链接
            const detailUrl = this.dataset.detailUrl;
            if (detailUrl) {
                // 跳转到任务详情页面!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                // window.location.href = detailUrl;
            }

            // 判断是否已经点击过该项
            const clicked = clickedItems.includes(item);
            if (!clicked) {
                // 删除之前点击的项对应的 alert 元素
                const previousClickedItem = clickedItems[0];
                if (previousClickedItem) {
                    const previousAlertElement = previousClickedItem.querySelector('.col-auto #alert');
                    if (previousAlertElement) {
                        previousAlertElement.remove();
                    }
                }

                // 删除当前项对应的 alert 元素
                const alertElement = item.querySelector('.col-auto #alert');
                if (alertElement) {
                    alertElement.remove();
                }

                // 将当前项添加到已点击项数组中
                clickedItems = [item];
            }
        });
    });

    // 为复选框添加事件监听器
    document.querySelectorAll('.list-group-item .form-check-input').forEach(checkbox => {
        const textElements = checkbox.closest('.list-group-item').querySelectorAll('.col.me-2');

        checkbox.addEventListener('change', function() {
            textElements.forEach(element => {
                const strong = element.querySelector('strong');
                const span = element.querySelector('span');

                if (this.checked) {
                    strong.style.textDecoration = 'line-through';
                    span.style.textDecoration = 'line-through';
                } else {
                    strong.style.textDecoration = 'none';
                    span.style.textDecoration = 'none';
                }
            });
        });
    });
});








// document.addEventListener("DOMContentLoaded", function() {
//     // 存储已点击项的数组
//     let clickedItems = [];

//     // 获取所有的 list-group-item 元素
//     const listItems = document.querySelectorAll('.list-group-item');

//     // 遍历所有的 list-group-item 元素
//     listItems.forEach(item => {
//         // 判断该项是否在 clickedItems 数组中
//         const clicked = clickedItems.includes(item);
//         if (clicked) {
//             const alertElement = document.getElementById('alert');
//             if (alertElement) {
//               alertElement.remove();
//             }
            
//         }

//         // 为每个 list-group-item 添加点击事件监听器
//         item.addEventListener('click', function() {
//             //获取任务详情链接
//             const detailUrl = this.dataset.detailUrl;
//             if (detailUrl) {
//                 // 跳转到任务详情页面!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//                 // window.location.href = detailUrl;
//             }
//             // 判断是否已经点击过该项
//             const clicked = clickedItems.includes(item);
//             if (!clicked) {
//                 const alertElement = document.getElementById('alert');
//                 if (alertElement) {
//                   alertElement.remove();
//                 }
                
//                 // 将该项添加到已点击项数组中
//                 clickedItems.push(item);
//             }
//         });
//     });
// });

// document.querySelectorAll('.list-group-item').forEach(item => {
//     const checkbox = item.querySelector('.form-check-input');
//     const textElements = item.querySelectorAll('.col.me-2');

//     checkbox.addEventListener('change', function() {
//         textElements.forEach(element => {
//             const strong = element.querySelector('strong');
//             const span = element.querySelector('span');

//             if (this.checked) {
//                 strong.style.textDecoration = 'line-through';
//                 span.style.textDecoration = 'line-through';
//             } else {
//                 strong.style.textDecoration = 'none';
//                 span.style.textDecoration = 'none';
//             }
//         });
//     });
// });
