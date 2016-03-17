/**
 * Created by 祥祥 on 2016/3/17.
 */
// 生成七牛key
function generatorKey(){
    var nub=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    var key;
    var randomLength = 8;
    var oDate=new Date();
    key=tenword(oDate.getFullYear())+tenword(oDate.getMonth()+1)+tenword(oDate.getDate())+tenword(oDate.getHours())+tenword(oDate.getMinutes())+tenword(oDate.getSeconds());
    for(var i = 0; i < randomLength; i ++)
    {
        key += nub[Math.floor(Math.random()*62)];
    }
    return '00' + key + '.jpg';
}
function tenword(n)
{
    if(n<10)
    {
        return "0"+n;
    }
    else if(n>=10)
    {
        return n+"";
    }
}