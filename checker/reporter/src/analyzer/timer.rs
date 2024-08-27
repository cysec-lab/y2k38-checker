use std::time::Instant;

pub struct Timer {
    time: f64,
    start_time: Option<Instant>,
}

impl Timer {
    pub fn new() -> Self {
        Timer {
            time: 0.0,
            start_time: None,
        }
    }

    pub fn start(&mut self) {
        self.start_time = Some(Instant::now());
    }

    pub fn stop(&mut self) {
        if let Some(start_time) = self.start_time {
            self.time = start_time.elapsed().as_secs_f64();
        }
    }

    pub fn time(&self) -> f64 {
        self.time
    }
}

impl Default for Timer {
    fn default() -> Self {
        Self::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::thread::sleep;
    use std::time::Duration;

    #[test]
    fn test_timer() {
        let mut timer = Timer::new();

        timer.start();
        sleep(Duration::from_secs(1));
        timer.stop();

        let elapsed_time = timer.time;
        assert!(
            (1.0..1.2).contains(&elapsed_time),
            "Elapsed time should be around 1 second"
        );
    }

    #[test]
    fn test_timer_without_start() {
        let mut timer = Timer::new();

        timer.stop();
        let elapsed_time = timer.time();

        assert_eq!(elapsed_time, 0.0);
    }
}
