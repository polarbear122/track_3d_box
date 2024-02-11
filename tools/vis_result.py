import json


def read_json(path):
    with open(path) as f:
        country_dict = json.load(f)
    return country_dict


def read_result_json():
    path = 'result/det-4d-depth/results.json'
    ans = read_json(path)
    for k in ans['results']:
        val = ans['results'][k]
        if len(val) > 500:
            min_score = 1
            track_arr = []
            for track in val:
                score = track['tracking_score']
                min_score = min(min_score, score)
                if score >= 0.01:
                    track_arr.append(track)
            print(min_score)
            print(k, len(track_arr))
            ans['results'][k] = track_arr
    write_json('res.json', ans)
    pass


def read_center_point_result():
    # simple track 验证集的追踪结果追踪结果 #6019 'fd8420396768425eabec9bdddf7e64b6'
    # path = 'preprocessing/nuscenes_data/centerpoint_val_result/pred.json'

    # simple track 测试集的追踪结果 #6008 '1b9a789e08bb4b7b89eacb2176c70840'
    # path = 'result/centerpoint/simpletrack2hz_nuscenes_test/results.json'

    # simple track 测试集的追踪结果 10hz 10hz 6008 '1b9a789e08bb4b7b89eacb2176c70840'
    # path = 'result/centerpoint/simpletrack10hz_nuscenes_test/results.json'

    # centerpoint检测结果 20hz 58431张 47d2f6131ba449f6a03ced4bde2c6dbe
    # path = 'result/centerpoint/detection-test-20hz.json'

    # centerpoint检测结果 2hz 6008张  1b9a789e08bb4b7b89eacb2176c70840
    # path = 'result/centerpoint/centerpoint_detect_test/infos_test_10sweeps_withvelo.json'

    # centerpoint 追踪结果 2hz 6008张  1b9a789e08bb4b7b89eacb2176c70840
    path = 'result/centerpoint/simpletrack2hz_nuscenes_test/mytrack/results.json'

    # centerpoint检测结果 #6019 'fd8420396768425eabec9bdddf7e64b6'
    # path = 'preprocessing/nuscenes_data/centerpoint_val_result/center_point_detection.json'

    ans = read_json(path)
    print(len(ans['results']))
    for k in ans['results']:
        val = ans['results'][k]
        print(k)
        break
        pass


# 拿到测试集的key集合
def convert_test_key_dict():
    path = 'result/centerpoint/simpletrack2hz_nuscenes_test/results.json'
    ans = read_json(path)
    print(len(ans['results']))
    test_keys = {}
    for k in ans['results']:
        val = ans['results'][k]
        test_keys[k] = 1
    write_json('result/test_keys.json', test_keys)


# 把centerpoint的20hz测试集检测结果，转换到2hz
# error，无法转换。因为20hz数据并不包含2hz数据
def coonvert_20hz_to_2hz():
    test_keys_path = 'result/test_keys.json'
    test_keys = read_json(test_keys_path)
    ans = read_json('result/centerpoint/detection-test-20hz.json')
    print(len(ans['results']))
    det_centerpoint_2hz_test = {}
    for k in ans['results']:
        val = ans['results'][k]
        if k in test_keys:
            det_centerpoint_2hz_test[k] = val
    write_json('result/detection_centerpoint_2hz_test.json', det_centerpoint_2hz_test)


def write_json(path, file):
    with open(path, 'w') as f:
        json.dump(file, f)


def read_npz():
    import numpy as np
    ac = np.load('result/scene-0077 (1).npz',allow_pickle=True)
    file = ac.files
    for f in file:
        x = ac[f]


if __name__ == '__main__':
    read_center_point_result()
