use pyo3::prelude::*;

#[pyclass]
struct Complex {
    real: f64,
    imag: f64
}

#[pymethods]
impl Complex {
    #[new]
    fn new(real: f64, imag: f64) -> Self {
        return Complex {
            real: real,
            imag: imag
        };
    }

    fn add(&self, other: &Self) -> Self {
        return Self::new(self.real + other.real, self.imag + other.imag);
    }

    fn sub(&self, other: &Self) -> Self {
        return Self::new(self.real - other.real, self.imag - other.imag);
    }

    fn mul(&self, other: &Self) -> Self {
        let new_real = self.real * other.real - self.imag * other.imag;
        let new_imag = self.real * other.imag + self.imag * other.real;
        return Self::new(new_real, new_imag);
    }

    fn dist_from_origin(&self) -> f64 {
        return (self.real.powi(2) + self.imag.powi(2)).sqrt()
    }
}

#[pyfunction]
fn simple_stability(real:f64, imag:f64, max_iterations:usize) -> usize {
    let mut zr = 0f64;
    let mut zi = 0f64;
    for i in 0..max_iterations {
        let new_zr = zr.powi(2) - zi.powi(2) + real;
        zi = 2.0 * zr * zi + imag;
        zr = new_zr;
        if (zr.powi(2) + zi.powi(2)).sqrt() > 2.0 {
            return i;
        }
    }
    return max_iterations;
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn mandelbrot_module(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(simple_stability, m)?)?;
    m.add_class::<Complex>()?;

    Ok(())
}