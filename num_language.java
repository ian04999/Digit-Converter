import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class num_language {
	public static void main(String[] args) {
		Map<String, Integer> map = new HashMap<>();
		String hundred = "hundred";
		String thousand = "thousand";
		String million = "million";
		String billion = "billion";

		// Adding key-value pairs
		map.put(1, "one");
		map.put(2, "two");
		map.put(3, "three");
		map.put(4, "four");
		map.put(5, "five");
		map.put(6, "six");
		map.put(7, "seven");
		map.put(8, "eight");
		map.put(9, "nine");
		map.put(10, "ten");
		map.put(11, "eleven");
		map.put(12, "twelve");
		map.put(13, "thirteen");
		map.put(14, "fourteen");
		map.put(15, "fifteen");
		map.put(16, "sixteen");
		map.put(17, "seventeen");
		map.put(18, "eighteen");
		map.put(19, "nineteen");
		map.put(20, "twenty");
		map.put(30, "thirty");
		map.put(40, "fourty");
		map.put(50, "fifty");
		map.put(60, "sixty");
		map.put(70, "seventy");
		map.put(80, "eighty");
		map.put(90, "ninety");
		
		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter an integer (greater than 0): ");

		int N = 0;
		String input = scanner.nextLine();
		int num_dig = input.length();
		try {
			N = Integer.parseInt(input);
			if (N < 0) {
				System.out.print("Please enter an Positive integer");
				return;
			} else if (N == 0) {
				System.out.print("zero");
			}
		} catch (NumberFormatException e) {
			System.out.println("Invalid input. Please enter a valid number.");
		}
		
		//call functions
		output(N, num_dig);
		
		scanner.close();
		
		/*
		// Accessing values by key
		System.out.println("Value corresponding to key 'Two': " + map.get("Two"));

		// Iterating through the map
		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			System.out.println(entry.getKey() + ": " + entry.getValue());
		}
		int result = add(5, 3);
		System.out.println("Sum: " + result);
		*/
	}
	
	public static void output(HashMap hashMap, int N, int num_dig){
		String output = "";
		if (num_dig < 2){
			String foundKey = findKeyByValue(hashMap, N);
			if (foundKey != null) {
				output = foundKey;
			} else {
				int f_digit = foundKey/10*10;
				int s_digit = foundKey - f_digit;
				String foundFKey = findKeyByValue(hashMap, f_digit);
				String foundSKey = findKeyByValue(hashMap, s_digit);
				output = foundFKey + " " + foundSKey;
			}
		} else {
			System.out.print("Not yet");
		}
		System.out.print(output);
	}
	
	// Method to find a key based on a value in a HashMap
    private static <K, V> K findKeyByValue(Map<K, V> map, V value) {
        for (Map.Entry<K, V> entry : map.entrySet()) {
            if (value.equals(entry.getValue())) {
                return entry.getKey();
            }
        }
        return null; // Value not found
    }
}