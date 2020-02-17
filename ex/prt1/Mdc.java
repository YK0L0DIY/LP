public class Mdc{

    int num1;
    int num2;

    public mdc(int a,int b){
        this.num1=a;
        this.num2=b;
    }

    public int calc(){
        if (this.num1==this.num2){
            return this.num1;
        }else if(this.num2>this.num1){
            this.num2-=this.num1;
            return calc();
        }else{
            this.num1-=this.num2;
            return calc();
        }
    }
}

