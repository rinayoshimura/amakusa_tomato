$(function() {
	setTimeout(function(){
		$('.start p').fadeIn(1600);
	},500); //0.5秒後にロゴをフェードイン!
	setTimeout(function(){
		$('.start').fadeOut(500);
	},2500); //2.5秒後にロゴ含め真っ白背景をフェードアウト！
});
// ------------------------------------------------------------
// 確認ボタン付きのダイアログボックスを表示して結果を得る
// ------------------------------------------------------------
function check(){
    var result = confirm( "完全削除？" );

    if(result){
	    console.log(" OK ");
        return true;

    }else{
	    console.log(" CANCEL ");
        return false;
    }
}tr



// $(function() {
//     alert('OK!');
//   });