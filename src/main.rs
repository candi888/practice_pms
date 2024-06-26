use ndarray::*;

fn set_initial_position(
    pos: &mut Array2<f64>,
    disa: &Array1<f64>,
    num_particles: usize,
    dim: usize,
) {
    for i in 0..num_particles {
        for j in 0..dim {
            if j == 0 {
                pos[[i, j]] = i as f64 * disa[i]
            } else {
                pos[[i, j]] = 0.0;
            };
        }
    }
}

// [kg,m,s　単位系]
fn main() {
    //! 配列などの初期設定
    const NUM_PARTICLES: usize = 100;
    const DIM: usize = 2;
    const DISA0: f64 = 1.0;
    const G: f64 = 9.8;
    let mut pos = Array2::from_shape_vec(
        (NUM_PARTICLES, DIM),
        vec![10_f64.powi(10_i32); NUM_PARTICLES * 2],
    )
    .unwrap();
    let disa = Array1::from_shape_vec(NUM_PARTICLES, vec![DISA0; NUM_PARTICLES]).unwrap();

    set_initial_position(&mut pos, &disa, NUM_PARTICLES, DIM);

    println!("{:?}", pos);
}
