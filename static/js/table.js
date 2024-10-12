var table = document.getElementById("dataTable");
var select = document.querySelector("#dataTable_length select");
var infoElement = document.getElementById("dataTable_info");
var pagination = document.querySelector(".pagination");

select.addEventListener("change", function() {
    var pageSize = parseInt(select.value);
    var rows = table.getElementsByTagName("tbody")[0].getElementsByTagName("tr");
    var pageCount = Math.ceil(rows.length / pageSize);
    updateTable(1, pageSize, pageCount);
});

var pageSize = parseInt(select.value);
var rows = table.getElementsByTagName("tbody")[0].getElementsByTagName("tr");
var pageCount = Math.ceil(rows.length / pageSize);
updateTable(1, pageSize, pageCount);

function updateTable(currentPage, pageSize, pageCount) {
    var startRowIndex = (currentPage - 1) * pageSize;
    var endRowIndex = startRowIndex + pageSize;
    var totalRowCount = rows.length;

    for (var i = 0; i < rows.length; i++) {
        if (i >= startRowIndex && i < endRowIndex) {
            rows[i].style.display = ""; // 显示当前页的行
        } else {
            rows[i].style.display = "none"; // 隐藏其他行
        }
    }

    pagination.innerHTML = ""; // 清空分页导航栏的内容

    var prevButton = document.createElement("li"); // 创建上一页按钮元素
    prevButton.className = "page-item";
    if (currentPage === 1) {
        prevButton.className += " disabled";
    }
    prevButton.innerHTML = '<a class="page-link" aria-label="Previous" href="#" onclick="updateTable(' + (currentPage - 1) + ',' + pageSize + ',' + pageCount + ')"><span aria-hidden="true">«</span></a>';
    pagination.appendChild(prevButton); // 添加上一页按钮

    for (var i = 0; i < pageCount; i++) {
        var pageNumber = i + 1;

        var pageButton = document.createElement("li"); // 创建页码按钮元素
        pageButton.className = "page-item";
        if (pageNumber === currentPage) {
            pageButton.className += " active"; // 将当前页码按钮设置为活动状态
        }
        pageButton.innerHTML = '<a class="page-link" href="#" onclick="updateTable(' + pageNumber + ',' + pageSize + ',' + pageCount + ')">' + pageNumber + '</a>';
        pagination.appendChild(pageButton); // 添加页码按钮
    }

    var nextButton = document.createElement("li"); // 创建下一页按钮元素
    nextButton.className = "page-item";
    if (currentPage === pageCount) {
        nextButton.className += " disabled";
    }
    nextButton.innerHTML = '<a class="page-link" aria-label="Next" href="#" onclick="updateTable(' + (currentPage + 1) + ',' + pageSize + ',' + pageCount + ')"><span aria-hidden="true">»</span></a>';
    pagination.appendChild(nextButton); // 添加下一页按钮

    var startRowCount = startRowIndex + 1; // 当前页的起始行数
    var endRowCount = Math.min(endRowIndex, totalRowCount); // 当前页的结束行数

    infoElement.textContent = "Showing " + startRowCount + " to " + endRowCount + " of " + totalRowCount; // 更新显示信息文本
}