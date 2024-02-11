# 首先按照https://github.com/tusen-ai/SimpleTrack/blob/main/docs/data_preprocess.md进行预处理，处理nuscenes
cd preprocessing/nuscenes_data
# 生成真实标注
bash nuscenes_preprocess.sh ${raw_data_dir} ${data_dir_2hz} ${data_dir_20hz}
# 然后输入结果results_nusc.json，得到输出
python detection.py --raw_data_folder ~/nuScenceData/nuscenes/ --data_folder data_dir_2hz --det_name 4d_depth_eval --file_path results_nusc.json --mode 2hz --velo

# 之后run.sh
python tools/main_nuscenes.py \
    --name test \
    --det_name centerpoint_test_track_ans \
    --config_path configs/nu_configs/giou.yaml \
    --result_folder cp_test_track_ans \
    --data_folder preprocessing/nuscenes_data/data_dir_2hz \
    --process 150

#再之后convert.sh
python tools/nuscenes_result_creation.py \
    --name test_track_alltype \
    --result_folder ./cp_test_track_ans \
    --data_folder preprocessing/nuscenes_data/data_dir_2hz/  --test

python tools/nuscenes_type_merge.py \
    --name test_track_alltype \
    --result_folder cp_test_track_ans

python tools/eval.py