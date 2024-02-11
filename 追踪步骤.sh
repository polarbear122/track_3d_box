# 首先按照https://github.com/tusen-ai/SimpleTrack/blob/main/docs/data_preprocess.md进行预处理，处理nuscenes
cd preprocessing/nuscenes_data
# 生成真实标注
bash nuscenes_preprocess.sh ${raw_data_dir} ${data_dir_2hz} ${data_dir_20hz}
# 然后输入结果results_nusc.json，得到输出
python detection.py --raw_data_folder ~/nuScenceData/nuscenes/ --data_folder data_dir_2hz --det_name cp_test_my --file_path results_nusc.json --mode 2hz --velo

#python tools/main_nuscenes.py --name pedmy --det_name centerpoint_eval/ --config_path configs/nu_configs/mygiou.yaml --result_folder cp_val_res --data_folder preprocessing/nuscenes_data/data_dir_2hz  --process 150 --obj_types pedestrian
# 之后run.sh
python tools/main_nuscenes.py \
    --name ped_my \
    --det_name cp_test \
    --config_path configs/nu_configs/mygiou.yaml \
    --result_folder cp_test_track_ans \
    --data_folder preprocessing/nuscenes_data/data_dir_2hz \
    --process 20 --obj_types pedestrian --test

#再之后convert.sh
python tools/nuscenes_result_creation.py \
    --name ped_my \
    --result_folder ./cp_test_track_ans \
    --data_folder preprocessing/nuscenes_data/data_dir_2hz/  --test --obj_types pedestrian

python tools/nuscenes_type_merge.py \
    --name ped_my \
    --result_folder cp_test_track_ans --obj_types pedestrian

python tools/eval.py