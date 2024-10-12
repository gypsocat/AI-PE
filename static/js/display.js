// JS代码
function toggleTheme() {
    var stickyHeader = document.getElementById("sticky-header");
    if (stickyHeader.classList.contains("dark"))
        stickyHeader.classList.remove("dark");
    else
        stickyHeader.classList.add("dark");
}
