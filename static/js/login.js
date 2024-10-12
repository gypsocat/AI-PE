var ID,password,Identity
// (function(){
//     //Login/Signup modal window - by CodyHouse.co
// 	function ModalSignin( element ) {
// 		this.element = element;
// 		this.blocks = this.element.getElementsByClassName('js-signin-modal-block');
// 		this.switchers = this.element.getElementsByClassName('js-signin-modal-switcher')[0].getElementsByTagName('a'); 
// 		this.triggers = document.getElementsByClassName('js-signin-modal-trigger');
// 		this.hidePassword = this.element.getElementsByClassName('js-hide-password');
// 		this.init();
// 	};

// 	ModalSignin.prototype.init = function() {
// 		var self = this;
// 		//open modal/switch form
// 		for(var i =0; i < this.triggers.length; i++) {
// 			(function(i){
// 				self.triggers[i].addEventListener('click', function(event){
// 					if( event.target.hasAttribute('data-signin') ) {
// 						event.preventDefault();
// 						self.showSigninForm(event.target.getAttribute('data-signin'));
// 					}
// 				});
// 			})(i);
// 		}

// 		//close modal
// 		this.element.addEventListener('click', function(event){
// 			if( hasClass(event.target, 'js-signin-modal') || hasClass(event.target, 'js-close') ) {
// 				event.preventDefault();
// 				removeClass(self.element, 'cd-signin-modal--is-visible');
// 			}
// 		});
// 		//close modal when clicking the esc keyboard button
// 		document.addEventListener('keydown', function(event){
// 			(event.which=='27') && removeClass(self.element, 'cd-signin-modal--is-visible');
// 		});

// 		//hide/show password
// 		for(var i =0; i < this.hidePassword.length; i++) {
// 			(function(i){
// 				self.hidePassword[i].addEventListener('click', function(event){
// 					self.togglePassword(self.hidePassword[i]);
// 				});
// 			})(i);
// 		} 

// 		//IMPORTANT - REMOVE THIS - it's just to show/hide error messages in the demo
// 		this.blocks[0].getElementsByTagName('form')[0].addEventListener('submit', function(event){
// 			event.preventDefault();
// 			self.toggleError(document.getElementById('signin-email'), true);
// 		});
// 		this.blocks[1].getElementsByTagName('form')[0].addEventListener('submit', function(event){
// 			event.preventDefault();
// 			self.toggleError(document.getElementById('signup-username'), true);
// 		});
// 	};

// 	ModalSignin.prototype.togglePassword = function(target) {
// 		var password = target.previousElementSibling;
// 		( 'password' == password.getAttribute('type') ) ? password.setAttribute('type', 'text') : password.setAttribute('type', 'password');
// 		target.textContent = ( 'Hide' == target.textContent ) ? 'Show' : 'Hide';
// 		putCursorAtEnd(password);
// 	}

// 	ModalSignin.prototype.showSigninForm = function(type) {
// 		// show modal if not visible
// 		!hasClass(this.element, 'cd-signin-modal--is-visible') && addClass(this.element, 'cd-signin-modal--is-visible');
// 		// show selected form
// 		for( var i=0; i < this.blocks.length; i++ ) {
// 			this.blocks[i].getAttribute('data-type') == type ? addClass(this.blocks[i], 'cd-signin-modal__block--is-selected') : removeClass(this.blocks[i], 'cd-signin-modal__block--is-selected');
// 		}
// 		//update switcher appearance
// 		var switcherType = (type == 'signup') ? 'signup' : 'login';
// 		for( var i=0; i < this.switchers.length; i++ ) {
// 			this.switchers[i].getAttribute('data-type') == switcherType ? addClass(this.switchers[i], 'cd-selected') : removeClass(this.switchers[i], 'cd-selected');
// 		} 
// 	};

// 	ModalSignin.prototype.toggleError = function(input, bool) {
// 		// used to show error messages in the form
// 		toggleClass(input, 'cd-signin-modal__input--has-error', bool);
// 		toggleClass(input.nextElementSibling, 'cd-signin-modal__error--is-visible', bool);
// 	}

// 	var signinModal = document.getElementsByClassName("js-signin-modal")[0];
// 	if( signinModal ) {
// 		new ModalSignin(signinModal);
// 	}

// 	// toggle main navigation on mobile
// 	var mainNav = document.getElementsByClassName('js-main-nav')[0];
// 	if(mainNav) {
// 		mainNav.addEventListener('click', function(event){
// 			if( hasClass(event.target, 'js-main-nav') ){
// 				var navList = mainNav.getElementsByTagName('ul')[0];
// 				toggleClass(navList, 'cd-main-nav__list--is-visible', !hasClass(navList, 'cd-main-nav__list--is-visible'));
// 			} 
// 		});
// 	}
	
// 	//class manipulations - needed if classList is not supported
// 	function hasClass(el, className) {
// 	  	if (el.classList) return el.classList.contains(className);
// 	  	else return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'));
// 	}
// 	function addClass(el, className) {
// 		var classList = className.split(' ');
// 	 	if (el.classList) el.classList.add(classList[0]);
// 	 	else if (!hasClass(el, classList[0])) el.className += " " + classList[0];
// 	 	if (classList.length > 1) addClass(el, classList.slice(1).join(' '));
// 	}
// 	function removeClass(el, className) {
// 		var classList = className.split(' ');
// 	  	if (el.classList) el.classList.remove(classList[0]);	
// 	  	else if(hasClass(el, classList[0])) {
// 	  		var reg = new RegExp('(\\s|^)' + classList[0] + '(\\s|$)');
// 	  		el.className=el.className.replace(reg, ' ');
// 	  	}
// 	  	if (classList.length > 1) removeClass(el, classList.slice(1).join(' '));
// 	}
// 	function toggleClass(el, className, bool) {
// 		if(bool) addClass(el, className);
// 		else removeClass(el, className);
// 	}

// 	//credits http://css-tricks.com/snippets/jquery/move-cursor-to-end-of-textarea-or-input/
// 	function putCursorAtEnd(el) {
//     	if (el.setSelectionRange) {
//       		var len = el.value.length * 2;
//       		el.focus();
//       		el.setSelectionRange(len, len);
//     	} else {
//       		el.value = el.value;
//     	}
// 	};
// })();


//---------------------这里的代码要改-----------------------
document.getElementById('loginButton').addEventListener('click', function() {
	event.preventDefault();
    console.log("Button clicked");
    ID = document.getElementById("exampleInputID").value;
    password = document.getElementById("exampleInputPassword").value;
    identity = document.getElementById("identity").value;
    console.log("ID:", ID);
    console.log("Password:", password);
    console.log("Identity:",identity);
	console.log(identity);

});

//===================================================这个部分有身份认证，会验证输入的账号和密码，但为了方便，先注释到这一段，只按照身份跳转页面=======================================
// document.getElementById('loginButton').addEventListener('click', async function(event) {
//     event.preventDefault(); // 阻止表单默认提交行为
//     var formData = {
//         'ID': document.getElementById('exampleInputID').value,
//         'password': document.getElementById('exampleInputPassword').value,
//         'identity': document.getElementById('identity').value
//     };
    
//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/', true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     xhr.onload = async function() {
//         if (xhr.status === 200) {
//             console.log('Response:', xhr.responseText);
//             var data = JSON.parse(xhr.responseText);
//             console.log("data:",data);
//             //获取 success 字段对应的值
//             var result = data.result
//             console.log("result:",result);
//             if(result)
//             {	// 根据身份执行不同操作
//                 console.log("result is true");
//                 if (identity === 'student') {
//                     console.log("Student Login");
//                     console.log("ID:",ID);
//                     await doXHRRequest("/student",ID); // 等待XHR请求完成
//                     window.location.href = "/student_proflie_mobile";
//                     console.log("goto other html");
//                 } else if (identity === 'teacher') {
//                     console.log('Teacher Login');
//                     await doXHRRequest("/teacher",ID); // 等待XHR请求完成
//                     window.location.href = "/teacher_profile";
//                     console.log("goto other html");
//                 }
//             } else {
//                 console.log("goto false one");
//                 var ID_input = document.getElementById("exampleInputID");
//                 // 检查输入框是否存在
//                 if (ID_input !== null) {
//                     // 清空输入框的值
//                     ID_input.value = "";
//                 } else {
//                     console.error("ID Input element not found!");
//                 }
//                 // 显示错误框
//                 var errorBox = document.getElementById("errorBox");
//                 errorBox.style.display = "block";

//                 // 一秒后隐藏错误框
//                 setTimeout(function() {
//                     errorBox.style.display = "none";
//                 }, 1600);
//             }
//         } else {
//             console.error('Request failed:', xhr.status);
//         }
//     };
//     xhr.onerror = function() {
//         console.error('Request failed');
//     };
//     xhr.send(JSON.stringify(formData));
// });

// async function doXHRRequest(url, userID) {
//     return new Promise((resolve, reject) => {
//         console.log("****************** userID:",userID);
//         var xhr = new XMLHttpRequest();
//         xhr.open('POST', url, true);
//         xhr.setRequestHeader('Content-Type', 'application/json');
//         xhr.onload = function() {
//             if (xhr.status === 200) {
//                 console.log('!!!!!!!!!!!!!!sport_record Response:', xhr.responseText);
//                 resolve(xhr.responseText);
//             } else {
//                 reject('XHR request failed');
//             }
//         };
//         xhr.onerror = function() {
//             reject('XHR request failed');
//         };
//         xhr.send(JSON.stringify({"user_id": userID }));
//     });
// }
//===================================================这个部分有身份认证，会验证输入的账号和密码，但为了方便，先注释到这一段，只按照身份跳转页面=======================================


// ==================  之后可删  =================
document.getElementById('loginButton').addEventListener('click', function(event) {
    event.preventDefault(); // 阻止表单默认提交行为
    identity = document.getElementById('identity').value;
    if (identity === 'student') {
        window.location.href = "/student_profile_mobile";
    } else if (identity === 'teacher') {
        window.location.href = "/teacher_profile"; 
     } else if (identity === 'admin'){
        window.location.href = "/admin_user_table"; 
     }

});
// ======================================




