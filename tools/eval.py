from os import path as osp
import mmcv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--track_json', help="track result json", type=str)
parser.add_argument('--out_path', help="save result path", type=str)
args = parser.parse_args()

version = 'v1.0-trainval'
# result_path = 'result/SimpleTrack2Hz/results/results.json'
# output_dir = 'res_depth_result_val/SimpleTrack2Hz/metric'
result_path = args.track_json
output_dir = args.out_path
data_root = '/home/um202170407/nuScenceData/nuscenes'
eval_set_map = {
    'v1.0-mini'    : 'mini_val',
    'v1.0-trainval': 'val',
    'v1.0-test'    : 'test',
}
from nuscenes.eval.tracking.evaluate import TrackingEval
from nuscenes.eval.common.config import config_factory as track_configs

cfg = track_configs("tracking_nips_2019")
nusc_eval = TrackingEval(
    config=cfg,
    result_path=result_path,
    eval_set=eval_set_map[version],
    output_dir=output_dir,
    verbose=True,
    nusc_version=version,
    nusc_dataroot=data_root
)
metrics = nusc_eval.main()
# record metrics
metrics = mmcv.load(osp.join(output_dir, 'metrics_summary.json'))
print(metrics)
