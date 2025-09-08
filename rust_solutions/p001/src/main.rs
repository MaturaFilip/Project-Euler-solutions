// Solution to problem 1
// Find the sum of all the multiples of 3 or 5 below 1000
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let below_number: u32 = args[1].parse().expect("Argument must be possitive integer");
    
    let sum_multiples: u32 = multiples(below_number); 

    println!("{sum_multiples}")
}


fn multiples(nums: u32) -> u32 {
    let mut sum: u32 = 0;

    for i in 1..nums as u32 {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i;
        }
    }
    return sum;
}
