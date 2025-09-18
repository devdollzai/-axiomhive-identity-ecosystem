use crate::dynamicquant::QuantizationLevel;

pub trait Hardware {
    fn get_optimal_quantization(&self) -> QuantizationLevel;
    fn quantize(&self, data: &[f32], level: QuantizationLevel) -> Vec<u8>;
    fn dequantize(&self, data: &[u8], level: QuantizationLevel) -> Vec<f32>;
}
