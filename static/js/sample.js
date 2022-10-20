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
