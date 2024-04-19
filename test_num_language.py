from num_language import testing

def test_simple():
    assert testing(1) == "one"
    assert testing(10) == "ten"
    assert testing(100) == "one hundred"
    assert testing(1000) == "one thousand "
    assert testing(10000) == "ten thousand "
    assert testing(100000) == "one hundred thousand "
    assert testing(1000000) == "one million "
    assert testing(10000000) == "ten million "
    assert testing(100000000) == "one hundred million "
    assert testing(1000000000) == "Over Billion"

def test_basic_1():
    assert testing(-1) == "Not Support Negative Number"
    assert testing(0) == "Zero"
    assert testing(1) == "one"
    assert testing(5) == "five"
    assert testing(9) == "nine"
    
def test_basic_2():
    assert testing(10) == "ten"
    assert testing(11) == "eleven"
    assert testing(12) == "twelve"
    assert testing(13) == "thirteen"
    assert testing(14) == "fourteen"
    assert testing(15) == "fifteen"
    assert testing(16) == "sixteen"
    assert testing(17) == "seventeen"
    assert testing(18) == "eightteen"
    assert testing(19) == "nineteen"
    assert testing(20) == "twenty "
    assert testing(21) == "twenty one"
    assert testing(25) == "twenty five"
    assert testing(29) == "twenty nine"
    assert testing(30) == "thirty "
    assert testing(32) == "thirty two"
    assert testing(36) == "thirty six"
    assert testing(38) == "thirty eight"
    assert testing(40) == "forty "
    assert testing(44) == "forty four"
    assert testing(50) == "fifty "
    assert testing(60) == "sixty "
    assert testing(70) == "seventy "
    assert testing(80) == "eighty "
    assert testing(88) == "eighty eight"
    assert testing(90) == "ninty "
    assert testing(99) == "ninty nine"
    
def test_basic_3():
    assert testing(100) == "one hundred"
    assert testing(111) == "one hundred eleven"
    assert testing(120) == "one hundred twenty "
    assert testing(113) == "one hundred thirteen"
    assert testing(124) == "one hundred twenty four"
    assert testing(150) == "one hundred fifty "
    assert testing(169) == "one hundred sixty nine"
    assert testing(197) == "one hundred ninty seven"
    assert testing(188) == "one hundred eighty eight"
    assert testing(179) == "one hundred seventy nine"
    assert testing(200) == "two hundred"
    assert testing(210) == "two hundred ten"
    assert testing(255) == "two hundred fifty five"
    assert testing(291) == "two hundred ninty one"
    assert testing(300) == "three hundred"
    assert testing(302) == "three hundred two"
    assert testing(360) == "three hundred sixty "
    assert testing(383) == "three hundred eighty three"
    assert testing(400) == "four hundred"
    assert testing(444) == "four hundred forty four"
    assert testing(500) == "five hundred"
    assert testing(600) == "six hundred"
    assert testing(700) == "seven hundred"
    assert testing(800) == "eight hundred"
    assert testing(880) == "eight hundred eighty "
    assert testing(900) == "nine hundred"
    assert testing(999) == "nine hundred ninty nine"

def test_basic_t():
    assert testing(1000) == "one thousand "
    assert testing(1001) == "one thousand one"
    assert testing(1020) == "one thousand twenty "
    assert testing(1300) == "one thousand three hundred"
    assert testing(1405) == "one thousand four hundred five"
    assert testing(1670) == "one thousand six hundred seventy "
    assert testing(1891) == "one thousand eight hundred ninty one"
    assert testing(1097) == "one thousand ninty seven"
    assert testing(2000) == "two thousand "
    assert testing(2010) == "two thousand ten"
    assert testing(2550) == "two thousand five hundred fifty "
    assert testing(2901) == "two thousand nine hundred one"
    assert testing(3000) == "three thousand "
    assert testing(3002) == "three thousand two"
    assert testing(3060) == "three thousand sixty "
    assert testing(3803) == "three thousand eight hundred three"
    assert testing(4000) == "four thousand "
    assert testing(4444) == "four thousand four hundred forty four"
    assert testing(5000) == "five thousand "
    assert testing(6000) == "six thousand "
    assert testing(7000) == "seven thousand "
    assert testing(8000) == "eight thousand "
    assert testing(8800) == "eight thousand eight hundred"
    assert testing(9000) == "nine thousand "
    assert testing(9999) == "nine thousand nine hundred ninty nine"

#5 digit
def test_basic_tt():
    assert testing(10000) == "ten thousand "
    assert testing(20001) == "twenty  thousand one"
    assert testing(30040) == "thirty  thousand forty "
    assert testing(40600) == "forty  thousand six hundred"
    assert testing(41000) == "forty one thousand "
    assert testing(44444) == "forty four thousand four hundred forty four"
    assert testing(50765) == "fifty  thousand seven hundred sixty five"
    assert testing(51003) == "fifty one thousand three"
    assert testing(61050) == "sixty one thousand fifty "
    assert testing(71500) == "seventy one thousand five hundred"
    assert testing(82908) == "eighty two thousand nine hundred eight"
    assert testing(99999) == "ninty nine thousand nine hundred ninty nine"

def test_basic_ht():
    assert testing(100000) == "one hundred thousand "
    #...
    assert testing(999999) == "nine hundred ninty nine thousand nine hundred ninty nine"
    
def test_main():
    print("<==============+ Simple test case +==============>")
    test_simple()
    print("\n<==============+ Basic test case 1 digit +==============>")
    test_basic_1()
    print("\n<==============+ Basic test case 2 digit +==============>")
    test_basic_2()
    print("\n<==============+ Basic test case 3 digit +==============>")
    test_basic_3()
    print("\n<==============+ Basic test case Thousand +==============>")
    test_basic_t()
    test_basic_tt()
    test_basic_ht()
    print("\n<==============+ Basic test case Million +==============>")
    print("\n<==============+ Basic test case Error +==============>")
    
    
test_main()