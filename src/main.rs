use ndarray::*;
use std::fs::create_dir_all;
use std::fs::File;
use std::io::Write;

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

fn value_force_gravity(m: &Array1<f64>, g: f64, num_particles: usize, dim: usize) -> Array2<f64> {
    let mut force_gravity =
        Array2::from_shape_vec((num_particles, dim), vec![0.0; num_particles * dim]).unwrap();

    for i in 0..num_particles {
        force_gravity[[i, 1]] = -m[i] * g;
    }

    force_gravity
}

fn update_velocity(
    vel: &mut Array2<f64>,
    m: &Array1<f64>,
    g: f64,
    delta_t: f64,
    num_particles: usize,
    dim: usize,
) {
    // DEMの計算　各粒子間でdelta_x_ijを計算（近傍粒子探索？一旦後回し？） -> クォータニオンで座標変換（回転はz,xi軸に対する外積を計算してそれで軸も回転角も一意に定まる？zetaとetaは向きはどうでもいいから一回の回転でOK?） -> DEMの接触力の計算（パラメータ4つ計算） -> 座標変換戻す
    for i in 0..num_particles {
        for j in 0..dim {
            vel[[i, j]] += value_force_gravity(m, g, num_particles, dim)[[i, j]] / m[i] * delta_t;
        }
    }
}

fn update_position(
    pos: &mut Array2<f64>,
    vel: &Array2<f64>,
    delta_t: f64,
    num_particles: usize,
    dim: usize,
) {
    pos.zip_mut_with(vel, |p, &v| {
        *p += v * delta_t;
    });
}

fn output_snap(
    pos: &Array2<f64>,
    vel: &Array2<f64>,
    disa: &Array1<f64>,
    cur_output_time_usize: usize,
    num_particles: usize,
    dim: usize,
    output_dir_path: &str,
) {
    let error_message: &str = "Unable to write data";
    // SNAP出力用のファイルを作成&開く
    let mut file = File::create(format!(
        "{}SNAP_{:05}.dat",
        output_dir_path, cur_output_time_usize
    ))
    .expect(error_message);
    // データ書き込み
    for i in 0..num_particles {
        for j in 0..dim {
            write!(file, "{} ", pos[[i, j]]).expect(error_message);
        }
        for j in 0..dim {
            write!(file, "{} ", vel[[i, j]]).expect(error_message);
        }
        write!(file, "{} ", disa[i]).expect(error_message);
        writeln!(file, "").expect(error_message);
    }
}

// [kg,m,s　単位系]
fn main() {
    //! 配列などの初期設定
    const NUM_PARTICLES: usize = 100;
    const DIM: usize = 2;
    const DISA0: f64 = 0.5;
    const m0: f64 = 1.0;
    let mut pos = Array2::from_shape_vec(
        (NUM_PARTICLES, DIM),
        vec![10_f64.powi(10_i32); NUM_PARTICLES * DIM],
    )
    .unwrap();
    let mut vel = Array2::from_shape_vec(
        (NUM_PARTICLES, DIM),
        vec![10_f64.powi(10_i32); NUM_PARTICLES * DIM],
    )
    .unwrap();
    let disa = Array1::from_shape_vec(NUM_PARTICLES, vec![DISA0; NUM_PARTICLES]).unwrap();
    let m = Array1::from_shape_vec(NUM_PARTICLES, vec![m0; NUM_PARTICLES]).unwrap();

    // 初期条件の設定
    set_initial_position(&mut pos, &disa, NUM_PARTICLES, DIM);
    set_initial_velocity(&mut vel, &disa, NUM_PARTICLES, DIM);

    const G: f64 = 9.8;
    let delta_t: f64 = 10.0_f64.powi(-4); //TODO constにしたい...
    let mut cur_t: f64 = 0.0;
    let output_time_interval_usize_ms: usize = 10;
    let mut next_output_time_usize: usize = 0;
    const TIME_MAX: f64 = 3.0;
    let time_step_max: usize = (TIME_MAX / delta_t) as usize; //TODO constにしたい...

    // データ出力用のディレクトリ作成
    let output_dir_path: &str = "./OUTPUT/";
    create_dir_all(output_dir_path).unwrap();
    // Execute Calulation
    for _ in 1..time_step_max {
        if cur_t > next_output_time_usize as f64 / 1000.0 {
            output_snap(
                &pos,
                &vel,
                &disa,
                next_output_time_usize,
                NUM_PARTICLES,
                DIM,
                output_dir_path,
            );
            next_output_time_usize += output_time_interval_usize_ms;
            println!("Output Time: {} ms", next_output_time_usize);
        }
        update_velocity(&mut vel, &m, G, delta_t, NUM_PARTICLES, DIM);
        update_position(&mut pos, &vel, delta_t, NUM_PARTICLES, DIM);
        cur_t += delta_t;
    }
}
