pub fn count_increments(input: Vec<usize>) -> usize {
    let mut prev_value = input[0];
    let mut increments = 0;
    for i in &input[1..] {
        if i > &prev_value {
            increments += 1;
        }
        prev_value = *i;
    }
    increments
}

pub fn generate_windows(input: Vec<usize>) -> Vec<Vec<usize>> {
    let mut windows: Vec<Vec<usize>> = Vec::new();
    for i in 0..input.len() {
        if input[i..].len() >= 3 {
            windows.push(input[i..i + 3].to_vec());
        }
    }
    windows
}

pub fn count_window_increments(input: Vec<usize>) -> usize {
    let windows = generate_windows(input);
    let mut prev_value: usize = windows[0].iter().sum();
    let mut increments = 0;
    for window in windows {
        let current_value: usize = window.iter().sum();
        if current_value > prev_value {
            increments += 1;
        }
        prev_value = current_value;
    }
    increments
}

#[cfg(test)]
mod tests {
    use crate::count_increments;
    use crate::count_window_increments;
    use crate::generate_windows;
    use shared::read_lines;
    use std::vec;

    #[test]
    #[ignore]
    fn d01_01() {
        let measurements = vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263];

        assert_eq!(count_increments(measurements), 7);
    }

    #[test]
    fn d01_02() {
        let lines = read_lines("./src/input.txt")
            .iter()
            .map(|f| f.parse().unwrap())
            .collect();

        assert_eq!(count_increments(lines), 1624);
    }

    #[test]
    fn d01_11() {
        let measurements = vec![607, 618, 618, 617, 647, 716, 769, 792];
        assert_eq!(generate_windows(measurements).len(), 6);
    }

    #[test]
    fn d01_12() {
        let measurements = vec![607, 618, 618, 617, 647, 716, 769, 792];
        assert_eq!(count_window_increments(measurements), 5);
    }

    #[test]
    fn d01_13() {
        let lines = read_lines("./src/input.txt")
            .iter()
            .map(|f| f.parse().unwrap())
            .collect();
        assert_eq!(count_window_increments(lines), 1653);
    }
}
