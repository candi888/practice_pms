import os
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib.font_manager import FontProperties, findSystemFonts
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.colorbar as colorbar
from matplotlib.cm import ScalarMappable, get_cmap
import matplotlib.ticker as mticker
from matplotlib.colors import Normalize, to_rgba
import matplotlib.patches as patches
from PIL import Image
import matplotlib as mpl
import matplotlib.style as mplstyle

#!フォント設定
plt.rcParams["font.family"] = "Times New Roman"  # font familyの設定
plt.rcParams["mathtext.fontset"] = "cm"  # math fontの設定
plt.rcParams["font.size"] = 18  # 全体のフォントサイズが変更されます。
# plt.rcParams['xtick.labelsize'] = 9 # 軸だけ変更されます。
# plt.rcParams['ytick.labelsize'] = 24 # 軸だけ変更されます
#!日本語フォント設定（old）
# font_paths = findSystemFonts()
# use_jp_font = [path for path in font_paths if "yumin.ttf" in path.lower()]
# assert len(use_jp_font) == 1
# jp_font = FontProperties(fname=use_jp_font[0], size=10)
jp_font_name = "MS Mincho"
jp_font_prop = FontProperties(family=jp_font_name)
#!軸設定
plt.rcParams["xtick.direction"] = "out"  # x軸の目盛りの向き
plt.rcParams["ytick.direction"] = "out"  # y軸の目盛りの向き
# plt.rcParams['axes.grid'] = True # グリッドの作成
# plt.rcParams['grid.linestyle']='--' #グリッドの線種
plt.rcParams["xtick.minor.visible"] = True  # x軸補助目盛りの追加
plt.rcParams["ytick.minor.visible"] = True  # y軸補助目盛りの追加
plt.rcParams["xtick.top"] = True  # x軸の上部目盛り
plt.rcParams["ytick.right"] = True  # y軸の右部目盛り
plt.rcParams["xtick.major.pad"] = 8.0  # distance to major tick label in points
plt.rcParams["ytick.major.pad"] = 5.0  # distance to major tick label in points
# plt.rcParams["axes.spines.top"] = False  # 上側の軸を表示するか#*
# plt.rcParams["axes.spines.right"] = False  # 右側の軸を表示するか

#!軸大きさ

# plt.rcParams["xtick.labelsize"] = 20.0  # 軸目盛のフォントサイズ変更
# plt.rcParams["ytick.labelsize"] = 20.0  # 軸目盛のフォントサイズ変更
# plt.rcParams["ytick.major.width"] = 1.0  # y軸主目盛り線の線幅
# plt.rcParams["xtick.minor.width"] = 1.0  # x軸補助目盛り線の線幅
# plt.rcParams["ytick.minor.width"] = 1.0  # y軸補助目盛り線の線幅
# plt.rcParams["xtick.major.width"] = 1.0             #x軸主目盛り線の線幅
# plt.rcParams["ytick.major.width"] = 1.0             #y軸主目盛り線の線幅
# plt.rcParams["xtick.minor.width"] = 1.0             #x軸補助目盛り線の線幅
# plt.rcParams["ytick.minor.width"] = 1.0             #y軸補助目盛り線の線幅
plt.rcParams["xtick.major.size"] = 5  # x軸主目盛り線の長さ
plt.rcParams["ytick.major.size"] = 5  # y軸主目盛り線の長さ
plt.rcParams["xtick.minor.size"] = 2  # x軸補助目盛り線の長さ
plt.rcParams["ytick.minor.size"] = 2  # y軸補助目盛り線の長さ
# plt.rcParams["axes.linewidth"] = 1.0                #囲みの太さ
#!凡例設定
plt.rcParams["legend.fontsize"] = 300  # 凡例のフォントサイズ
plt.rcParams["legend.fancybox"] = False  # 丸角OFF
plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = "black"  # edgeの色を変更
# plt.rcParams["legend.markerscale"] = 5  # markerサイズの倍率
#!svg保存用の設定
plt.rcParams["svg.fonttype"] = "none"
mpl.use("Agg")
# plt.rcParams['pdf.fonttype'] = 42
# plt.rcParams['ps.fonttype'] = 42
# * 以下，よく使うコマンドのメモ
# ax.set_xlabel(label="全断面に対する出現率", fontproperties=jp_font_name, x=0.85, labelpad=-10, rotation="horizontal") # 日本語の設定，位置調整など labelpadは30とかにしないと違い分からない
# ax.set_xlabel(r'分散（各y$座標ごと）', fontproperties=jp_font_prop) # texと日本語の混在
# 凡例表示
# ax.legend(
#     loc="upper left",
#      bbox_to_anchor=(1, 1),
#     prop={
#         "family": jp_font_name,
#         "size": 20,
#     },
# )


# # 基本日本語プロットはこうする？(old!!!!!!!)
# plt.rcParams['font.family'] = 'Yu Mincho'
# plt.legend()
# plt.rcParams['font.family'] = 'Times New Roman'

# # 余白調整&保存
# # 粒子のプロットだとscatterのサイズ計算が変になるので要修正？
# plt.subplots_adjust(left=0, right=1, bottom=0, top=1) # old
# plt.savefig(
#     f"{outdir}/danmen_appearrate.png",
#     bbox_inches="tight",
#     pad_inches=0.1,
#     transparent="True",
# )

# # 実験値のscatter plot
# ax.scatter(
#     exp[:, 0],
#     exp[:, 1],
#     label="exp 榊山（1997）",
#     marker="s",
#     facecolor="none",
#     edgecolors="#1f77b4",
#     linewidths=2,
#     s=200,
# )

# #軸を消す
# https://qiita.com/tsukada_cs/items/8d31a25cd7c860690270


inf = 1 << 61 - 1


def SetFrameRange_ByAllDAT(start_time, snap_interval_ms):
    int_second_starttime = int(start_time)
    print(int_second_starttime)
    for i in range(int_second_starttime, 100010, snap_interval_ms):
        cur_read_snap_path = (
            f"{SNAP_dir_path}{SNAP_file_prefix}{str(i).zfill(5)}.{SNAP_file_extension}"
        )
        if not os.path.isfile(cur_read_snap_path):
            frame_range = np.arange(int_second_starttime, i, snap_interval_ms)
            print("frame_range generate break ", cur_read_snap_path)
            break
    else:
        frame_range = None  # error

    return frame_range


# old
def GetXlimAndYlimByShoki():
    xudisa = np.loadtxt(f"./INPUT/XUDISA.DAT")
    par = xudisa[:, (0, 1, -1)]  # [x,y,disa]

    minx0, minx1 = np.amin(par[:, :], axis=0)[:2]
    maxx0, maxx1 = np.amax(par[:, :], axis=0)[:2]

    add_len_x0 = (maxx0 - minx0) / 20
    add_len_x1 = (maxx1 - minx1) / 20

    return (
        minx0 - add_len_x0,
        maxx0 + add_len_x0,
        minx1 - add_len_x1,
        maxx1 + add_len_x1,
    )


# old
def InitPlotForFixedWall(ax, snap_interval_ms):
    # 最初のプロットを使って差分更新と更新しないプロットを分ける
    xud = np.loadtxt(f"./OUTPUT/SNAP/XUD{str(snap_interval_ms*1).zfill(5)}.DAT")
    tmd = np.loadtxt(f"./OUTPUT/SNAP/TMD{str(snap_interval_ms*1).zfill(5)}.DAT")

    par = xud[:, (0, 1, 5)]  # [x,y,disa]
    nump = len(par)

    color = ["aqua", "rosybrown", "brown", "black", "violet", "magenta"]
    vector = np.vectorize(np.int_)
    par_color_idx = vector(tmd[:, (1)])  # [color]
    par_color = np.array([color[i] for i in par_color_idx])

    # ボトルネック
    circles = [
        patches.Circle((par[i, 0], par[i, 1]), par[i, -1] / 2)
        for i in range(len(par_color))
    ]
    idx_ax = set([i for i in range(nump) if par_color_idx[i] in {1, 2}])
    idx_sabun = set([i for i in range(nump) if par_color_idx[i] not in {1, 2}])
    circles_ax = [circles[i] for i in range(nump) if i in idx_ax]
    circles_sabun = [circles[i] for i in range(nump) if i in idx_sabun]
    color_ax = [par_color[i] for i in range(nump) if i in idx_ax]
    color_sabun = [par_color[i] for i in range(nump) if i in idx_sabun]

    # Collectionを作成して円を追加
    collection_ax = mcoll.PatchCollection(circles_ax, color=color_ax, linewidth=0)
    collection_sabun = mcoll.PatchCollection(
        circles_sabun, color=color_sabun, linewidth=0
    )

    # サブプロットにCollectionを追加
    ax.add_collection(collection_ax)
    sabun = ax.add_collection(collection_sabun)

    return sabun


# old
def GetParDat(cur_time):
    cur_read_snap_path = (
        f"{SNAP_dir_path}{SNAP_file_prefix}{str(i).zfill(5)}.{SNAP_file_extension}"
    )
    xud = np.loadtxt(f"./OUTPUT/SNAP/XUD{str(cur_time).zfill(5)}.DAT")

    x = xud[:, 0]
    y = xud[:, 1]
    r = xud[:, 5] / 2
    p = xud[:, 4]
    nump = len(x)

    assert nump == len(y) and nump == len(r) and nump == len(p)

    return x, y, r, p, nump


# old
def GetParColorByMove(cur_time):
    tmd = np.loadtxt(rf"./OUTPUT/SNAP/TMD{str(cur_time).zfill(5)}.DAT")

    color = ["aqua", "rosybrown", "brown", "black", "violet", "magenta"]
    vector = np.vectorize(np.int_)
    par_color_idx = vector(tmd[:, (1)])  # [color]
    par_color = np.array([color[i] for i in par_color_idx])

    return par_color


# old
def GetParColorByBconForHakokeisoku(cur_time):
    bcon = np.loadtxt(rf"./OUTPUT/SNAP/for_hako_keisoku{str(cur_time).zfill(5)}.DAT")
    vector = np.vectorize(np.int_)
    par_color_key = vector(bcon)

    # 0:水, 1: 自由表面, -1: ダミー, -2: 壁粒子
    color = {0: "aqua", -1: "red", -2: "black", 1: "yellow"}
    par_color = np.array([color[key] for key in par_color_key])

    return par_color


# old
def ChangeColorInPorousArea(x, y, par_color, nump):
    porous_area_vertex = np.loadtxt(rf"./INPUT/porous_area.dat")
    left, right = porous_area_vertex[0, 0], porous_area_vertex[3, 0]
    upper, lower = porous_area_vertex[0, 1], porous_area_vertex[1, 1]

    for i in range(nump):
        curx, cury = x[i], y[i]
        if left <= curx <= right and lower <= cury <= upper:
            par_color[i] = "blue"


# old
def ChangeColorOfWallPar(cur_time, par_color, change_color):
    tmd = np.loadtxt(rf"./OUTPUT/SNAP/TMD{str(cur_time).zfill(5)}.DAT")

    vector = np.vectorize(np.int_)
    par_color_idx = vector(tmd[:, (1)])  # [color]

    for i, pidx in enumerate(par_color_idx):
        if np.mod(pidx, 3) == 1:
            par_color[i] = to_rgba(change_color)
            # par_color[i] = (0, 0, 0, 0)  # 透明


# old
def ChangeColorOfDummyPar(cur_time, par_color, change_color):
    tmd = np.loadtxt(rf"./OUTPUT/SNAP/TMD{str(cur_time).zfill(5)}.DAT")

    vector = np.vectorize(np.int_)
    par_color_idx = vector(tmd[:, (1)])  # [color]

    for i, pidx in enumerate(par_color_idx):
        if np.mod(pidx, 3).astype(np.int_) == 2:
            par_color[i] = to_rgba(change_color)
            # par_color[i] = (0, 0, 0, 0)  # 透明


# old
def PlotBypatchcollection(ax, x, y, r, p, par_color, nump):
    circles = [patches.Circle((x[i], y[i]), r[i]) for i in range(nump)]

    # Collectionを作成して円を追加
    # 個々のオブジェクトのcolorを上書きしてしまうので注意
    collection = mcoll.PatchCollection(
        circles, match_original=True, facecolor=par_color, linewidth=0
    )

    # サブプロットにCollectionを追加
    ax.add_collection(collection)


def GetParColorByPressureContour(p, cmap, norm):
    par_color = cmap(norm(p))

    return par_color


#!　Colorbarのいろいろな調整
def PlotColorBar(ax, norm, cmap):
    mappable = ScalarMappable(cmap=cmap, norm=norm)
    mappable._A = []

    #! カラーバーの軸刻み
    ticks = np.linspace(norm.vmin, norm.vmax, 5)
    ticks = mticker.LinearLocator(numticks=5)

    #! 大きさと縦向き，横向き
    plt.colorbar(
        mappable,
        ax=ax,
        ticks=ticks,
        shrink=0.62,
        orientation="horizontal",
        pad=0.1,
    ).set_label(r"Pressure [Pa]")


#! 1フレームごとの描画の部分
# old
def update(frame, fig, ax, snap_interval_ms, minx, maxx, miny, maxy, cmap, norm):
    cur_time = frame * snap_interval_ms  # ms
    plt.cla()

    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)
    ax.set_xlabel(r"$x \mathrm{(m)}$")
    ax.set_ylabel(r"$y \mathrm{(m)}$")
    ax.minorticks_on()
    ax.set_title(rf"$t=$ {round(cur_time*1E-3,3):.2f}s")

    x, y, r, p, nump = GetParDat(cur_time)

    #! 色付け方法選択
    # par_color = GetParColorByMove(cur_time)
    par_color = GetParColorByPressureContour(p, cmap, norm)
    # par_color = GetParColorByBconForHakokeisoku(cur_time)

    #! Check Coloring Porous Area By Specific Color
    # ChangeColorInPorousArea(x, y, par_color, nump)

    #! Check Coloring WallPar Black
    ChangeColorOfWallPar(cur_time, par_color, change_color="black")
    ChangeColorOfDummyPar(cur_time, par_color, change_color="black")

    PlotByScatter(fig, ax, x, y, r, par_color, maxx, minx)

    #! SnapShot
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(
        f"{savedirname}/snap_shot/snap_{str(frame*snap_interval_ms).zfill(5)}.png",
        bbox_inches="tight",
        pad_inches=0.1,
    )

    print(f"{snap_interval_ms*frame/1000} finished")
    return


def CalcSizeForScatter(fig, ax, r, maxx, minx):
    ppi = 72
    ax_size_inch = ax.figure.get_size_inches()
    ax_w_inch = ax_size_inch[0] * (
        ax.figure.subplotpars.right - ax.figure.subplotpars.left
    )
    ax_w_px = ax_w_inch * fig.get_dpi()
    size = 2 * r[:] * (ax_w_px / (maxx - minx)) * (ppi / fig.dpi)

    return size


def PlotByScatter(fig, ax, x, y, r, par_color, maxx, minx):
    size = CalcSizeForScatter(fig, ax, r, maxx, minx)
    ax.scatter(x[:], y[:], linewidths=0, s=size**2, c=par_color[:])


def GetParDat_curusetmp(cur_time):
    cur_read_snap_path = f"{SNAP_dir_path}{SNAP_file_prefix}{str(cur_time).zfill(5)}.{SNAP_file_extension}"
    xud = np.loadtxt(cur_read_snap_path)

    x = xud[:, 0]
    y = xud[:, 1]
    r = xud[:, 4] / 2
    # p = xud[:, 4]
    nump = len(x)

    # assert nump == len(y) and nump == len(r) and nump == len(p)

    return x, y, r, nump


def MakeSnap(
    fig,
    ax,
    frame,
    cur_time,
    snap_interval_ms,
    cmap=None,
    norm=None,
    minx=None,
    maxx=None,
    miny=None,
    maxy=None,
):
    plt.cla()

    if minx is None and maxx is None and miny is None and maxy is None:
        pass
    elif (
        minx is not None and maxx is not None and miny is not None and maxy is not None
    ):
        ax.set_xlim(minx, maxx)
        ax.set_ylim(miny, maxy)
    else:
        raise ValueError("minx, maxx, miny, maxy is not None or all None")

    ax.set_xlabel(r"$x \mathrm{(m)}$")
    ax.set_ylabel(r"$y \mathrm{(m)}$")
    ax.minorticks_on()
    ax.set_title(rf"$t=$ {round(cur_time*1E-3,3):.2f}s")

    x, y, r, nump = GetParDat_curusetmp(cur_time)

    #! 色付け方法選択
    # TODO やる
    # par_color = GetParColorByMove(cur_time)
    # par_color = GetParColorByPressureContour(p, cmap, norm)
    # par_color = GetParColorByBconForHakokeisoku(cur_time)
    par_color = np.array(["black"] * nump)

    #! Check Coloring Porous Area By Specific Color
    # ChangeColorInPorousArea(x, y, par_color, nump)

    #! Check Coloring WallPar Black
    # ChangeColorOfWallPar(cur_time, par_color, change_color="black")
    # ChangeColorOfDummyPar(cur_time, par_color, change_color="black")

    PlotByScatter(
        fig,
        ax,
        x[:],
        y[:],
        np.full(nump, r[:], dtype=np.float64),
        par_color,
        maxx,
        minx,
    )

    #! SnapShot
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(
        f"{save_dir_path}snap_shot/snap_{str(cur_time).zfill(5)}.png",
        bbox_inches="tight",
        pad_inches=0.1,
    )

    print(f"{cur_time}[ms] finished")
    return


def MakeAnimation(savefilename, start_time):
    import subprocess

    ffmpeg_path = "ffmpeg"

    subprocess.run(
        [
            f"{ffmpeg_path}",
            "-y",
            "-framerate",
            "100",
            "-start_number",
            f"{start_time}",
            "-i",
            "snap_%*.png",
            "-vf",
            "scale=trunc(iw/2)*2:trunc(ih/2)*2",
            "-vcodec",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            f"../animation/{savefilename}.mp4",
        ],
        cwd=f"{save_dir_path}snap_shot",
    )


#! グローバル変数群
save_dir_path = "./plot_output/"
SNAP_dir_path = "./OUTPUT/"
SNAP_file_prefix = "SNAP_"
SNAP_file_extension = "dat"


#!　main部分
def main():
    flag_make_snap = True
    flag_make_animation = True

    #! 描画範囲を決める
    # minx, maxx, miny, maxy = GetXlimAndYlimByShoki()
    minx, maxx, miny, maxy = -10, 60, -50, 10
    print("minx, maxx, miny, maxy: ", minx, maxx, miny, maxy)

    #! Check dpi
    dpi = 100

    mplstyle.use("fast")

    # 出力用ディレクトリ作成
    os.makedirs(f"{save_dir_path}snap_shot", exist_ok=True)
    os.makedirs(f"{save_dir_path}animation", exist_ok=True)

    #! datファイルの00050のとこ.　SNAPの出力時間間隔が違う場合に注意
    snap_interval_ms = 10

    #! SNAP図示の開始時間 [ms]
    start_time = "0".zfill(5)

    #! Check 描画する時間範囲
    frame_range = SetFrameRange_ByAllDAT(start_time, snap_interval_ms)

    print(frame_range)
    print(f"animation range is: {frame_range[0]/1000}[s] ~ {frame_range[-1]/1000}[s]")

    fig = plt.figure(dpi=dpi)
    plt.clf()

    print("dpi is: ", dpi)
    ax = fig.add_subplot(1, 1, 1, aspect="equal")

    #! Check savefilename,　gifとmp4に対応
    savefilename = ""
    savefilename = f"{os.path.basename(os.getcwd())}"
    print("savefilename is: ", savefilename)

    # #! 圧力Contour図の場合---------------------------------------
    # #! 任意のカラーマップを選択
    # cmap = matplotlib.colormaps.get_cmap("rainbow")

    # #! 圧力コンターの最小，最大値設定
    # minp_for_coloring = 0
    # maxp_for_coloring = 1200

    # norm = Normalize(vmin=minp_for_coloring, vmax=maxp_for_coloring)

    # #! 手動で切り替え．．．
    # PlotColorBar(ax, norm, cmap)

    # #!----------------------------------------------------------

    if flag_make_snap:
        print("frame　作成開始")
        plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
        for frame, cur_time in enumerate(frame_range):
            MakeSnap(
                fig=fig,
                ax=ax,
                frame=frame + 1,
                cur_time=cur_time,
                snap_interval_ms=snap_interval_ms,
                minx=minx,
                maxx=maxx,
                miny=miny,
                maxy=maxy,
            )

    if flag_make_animation:
        print("animation　作成開始")
        MakeAnimation(savefilename, start_time)

    plt.close(fig)
    print("描画終了")


if __name__ == "__main__":
    main()
