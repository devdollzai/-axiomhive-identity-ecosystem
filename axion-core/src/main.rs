mod hal;
mod corelogic;
mod dynamicquant;

use hal::x86::X86CPU;
use crate::AxionCore;

fn main() {
    let hardware = X86CPU {};
    let mut core = AxionCore::new(hardware);
    let input = vec![0.1, 0.5, 0.9, 0.7];
    let output = core.execute(input);
    println!("Output: {:?}", output);
}
