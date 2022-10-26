$(function() {
	setTimeout(function(){
		$('.start p').fadeIn(1600);
	},5); //0.5秒後にロゴをフェードイン!
	setTimeout(function(){
		$('.start').fadeOut(500);
	},25); //2.5秒後にロゴ含め真っ白背景をフェードアウト！
});
// $(function() {
// 	setTimeout(function(){
// 		$('.start p').fadeIn(1600);
// 	},500); //0.5秒後にロゴをフェードイン!
// 	setTimeout(function(){
// 		$('.start').fadeOut(500);
// 	},2500); //2.5秒後にロゴ含め真っ白背景をフェードアウト！
// });


// ------------------------------------------------------------
// 確認ボタン付きのダイアログボックスを表示して結果を得る
// ------------------------------------------------------------
function check(){
    
	var result_1 = prompt("パスワードを入力してください");	

	password_tomato="1028"
	
	if(password_tomato==result_1){
		var result = confirm( "完全削除に削除しますか？" );
		if(result){
			console.log(" OK ");
			return true;
	
		}else{
			console.log(" CANCEL ");
			return false;
		}

	}else{
		var result = confirm( "パスワードが違います" );
		return false;
	}
    
}tr



// $(function() {
//     alert('OK!');
//   });