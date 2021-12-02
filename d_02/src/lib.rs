pub fn part1(input: Vec<String>) -> usize {
    let mut pos = 0;
    let mut depth = 0;
    let mut aim = 0;
    for i in input {
        let j = i.split_whitespace().collect::<Vec<&str>>();
        let command = j[0];
        let value = j[1].parse::<usize>().unwrap();
        match command {
            "up" => {
                aim -= value;
            }
            "down" => {
                aim += value;
            }
            "forward" => {
                pos += value;
                depth += aim * value;
            }
            _ => {
                panic!("Invalid input");
            }
        }
        println!("{} {} {}", pos, aim, depth);
        println!("{}", pos * depth);
    }
    pos * depth
}

#[cfg(test)]
mod tests {
    use crate::part1;
    use shared::read_lines;
    use std::vec;

    #[test]
    fn d02_01() {
        let lines = read_lines("./src/input.txt")
            .iter()
            .map(|f| f.parse().unwrap())
            .collect();

        assert_eq!(part1(lines), 1594785890);
    }
}
