import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;
import java.util.Contains;
public class tame {
    public static void main(String[] args){
        String[] str = {"AJ, Willy, billy"};
        Set<String> names = new HashSet<String>(Arrays.asList(str));
        System.out.println(names);
    }
    public static void data_description(){
        
    }
    public String checker(String name){
        String[] str = {"AJ, Willy, billy"};
        Set<String> nameset = new HashSet<String>(Arrays.asList(str));
        if (nameset.contains(name)){
            return ("Found name: %s" % name);
        }
    }
}