pub struct CoreState {}

impl CoreState {
    pub fn new() -> Self { Self {} }
    pub fn process(&self, input: &[u8]) -> Vec<u8> { input.to_vec() } // placeholder
}
