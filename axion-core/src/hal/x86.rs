use super::Hardware;
use crate::dynamicquant::QuantizationLevel;

pub struct X86CPU;

impl Hardware for X86CPU {
    fn get_optimal_quantization(&self) -> QuantizationLevel { QuantizationLevel::I8 }
    fn quantize(&self, data: &[f32], _level: QuantizationLevel) -> Vec<u8> {
        data.iter().map(|x| (*x * 100.0) as u8).collect()
    }
    fn dequantize(&self, data: &[u8], _level: QuantizationLevel) -> Vec<f32> {
        data.iter().map(|x| *x as f32 / 100.0).collect()
    }
}
