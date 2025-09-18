pub mod hal;
pub mod corelogic;
pub mod dynamicquant;

use hal::Hardware;
use dynamicquant::QuantizationLevel;

pub struct AxionCore<H: Hardware> {
    pub hardware: H,
    pub quantlevel: QuantizationLevel,
    pub corestate: corelogic::CoreState,
}

impl<H: Hardware> AxionCore<H> {
    pub fn new(hardware: H) -> Self {
        Self {
            hardware,
            quantlevel: QuantizationLevel::F32,
            corestate: corelogic::CoreState::new(),
        }
    }

    pub fn execute(&mut self, input: Vec<f32>) -> Vec<f32> {
        self.quantlevel = self.hardware.get_optimal_quantization();
        let quantized = self.hardware.quantize(&input, self.quantlevel);
        let processed = self.corestate.process(&quantized);
        self.hardware.dequantize(&processed, self.quantlevel)
    }
}
