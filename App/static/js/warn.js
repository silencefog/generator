function warning(){
        let f = parseInt(document.getElementById("first_id").value);
        let s = parseInt(document.getElementById("second_id").value);
            if(f > s){
                alert("Левая граница диапазона не может быть больше правой!")
                return false;
                }
            else{
                return true;
            }
        }