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

fn set_initial_velocity(
    vel: &mut Array2<f64>,
    disa: &Array1<f64>,
    num_particles: usize,
    dim: usize,
) {
    vel.fill(0.0);
}

fn update_velocity(vel: &mut Array2<f64>, g: f64, delta_t: f64, num_particles: usize) {
    for i in 0..num_particles {
        vel[[i, 0]] = vel[[i, 0]];
        vel[[i, 1]] = vel[[i, 1]] - g * delta_t;
    }
}

fn update_position(
    pos: &mut Array2<f64>,
    vel: &Array2<f64>,
    delta_t: f64,
    num_particles: usize,
    dim: usize,
) {
    for i in 0..num_particles {
        for j in 0..dim {
            pos[[i, j]] = pos[[i, j]] + vel[[i, j]] * delta_t;
        }
    }
}

// [kg,m,s　単位系]
fn main() {
    //! 配列などの初期設定
    const NUM_PARTICLES: usize = 100;
    const DIM: usize = 2;
    const DISA0: f64 = 1.0;
    const m0: f64 = 1.0;
    let mut pos = Array2::from_shape_vec(
        (NUM_PARTICLES, DIM),
        vec![10_f64.powi(10_i32); NUM_PARTICLES * 2],
    )
    .unwrap();
    let mut vel = Array2::from_shape_vec(
        (NUM_PARTICLES, DIM),
        vec![10_f64.powi(10_i32); NUM_PARTICLES * 2],
    )
    .unwrap();
    let disa = Array1::from_shape_vec(NUM_PARTICLES, vec![DISA0; NUM_PARTICLES]).unwrap();
    let m = Array1::from_shape_vec(NUM_PARTICLES, vec![m0; NUM_PARTICLES]).unwrap();

    set_initial_position(&mut pos, &disa, NUM_PARTICLES, DIM);
    set_initial_velocity(&mut vel, &disa, NUM_PARTICLES, DIM);

    const G: f64 = 9.8;
    let delta_t: f64 = 10.0_f64.powi(-4);
    const TIME_STEP_MAX: usize = 100001;
    for time_step in 1..TIME_STEP_MAX {
        update_velocity(&mut vel, G, delta_t, NUM_PARTICLES);
        update_position(&mut pos, &vel, delta_t, NUM_PARTICLES, DIM);

        if time_step % 1000 == 0 {
            println!("{:?}", time_step);
            println!("{:?}", pos[[0, 1]]);
            println!("{:?}", vel[[0, 1]]);
        }
    }
}
