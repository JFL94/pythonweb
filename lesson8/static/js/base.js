document.addEventListener('DOMContentLoaded', function () {
	const toggle = document.querySelector('.nav-toggle');
	const navList = document.querySelector('.nav-list');

	if (!toggle || !navList) return;

	toggle.addEventListener('click', function () {
		navList.classList.toggle('open');
	});

	// 在視窗尺寸改變到桌機時，自動關閉手機選單以避免遺留狀態
	window.addEventListener('resize', function () {
		if (window.innerWidth > 800) {
			if (navList.classList.contains('open')) {
				navList.classList.remove('open');
			}

			// 改變到桌機時，無執行toggle以下程式不需要
			/* 
				if (toggle.classList.contains('open')) {
				// 	toggle.classList.remove('open');
				// 	// toggle.setAttribute('aria-expanded', 'false');
				}
			*/
		}
	});
});