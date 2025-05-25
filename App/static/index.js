function loadnewpage() {
            fetch('/display')
                .then(response => response.text())
                .then(html => {
                    document.open();          // 清空整个 DOM
                    document.write(html);     // 写入新的 HTML
                    document.close();
                });
        }

// 监听右键菜单事件
window.onload = function() {
      document.addEventListener('contextmenu', function(e) {
        e.preventDefault(); // 阻止默认右键菜单弹出
        // 跳转到新页面，替换当前页面
        window.location.href = '/loaddb';  // 替换成新页面地址
      });
    }