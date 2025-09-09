// Solution to problem 2
// Find the sum of all even number in fibonacci sequence below 4_000_000
use std::env;

fn main() {
    // take number from command line (4_000_000)
    let args: Vec<String> = env::args().collect();
    let below_number: u32 = args[1].parse().expect("Argument must be possitive integer");
    
    let sum_even: u32 = fibonacci(below_number); 

    println!("{sum_even}")
}


fn fibonacci(max_num: u32) -> u32 {
    let mut sum: u32 = 0;
    let mut x1: u32 = 0;
    let mut x2: u32 = 1;

    loop {
        if x2 < max_num {
            let place_holder: u32 = x1 + x2;
            x1 = x2;
            x2 = place_holder;

            if x2 % 2 == 0 {
                sum += x2;
            }
        } else {
            break
        }
    }
    return sum;
}



