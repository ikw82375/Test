import json
import zipfile

# ZIPファイルのパス
zip_file_path = "kabeposter.zip"

# ZIPファイルを展開
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    file_path=zip_ref.namelist()
    for file_path in file_path:
        if file_path.endswith("00_keypoints.json"):
            with zip_ref.open(file_path, "r") as file:
                data=json.load(file)
    
# 2人の人の情報を取得
people=data["people"]
person1=people[0]
person2=people[1]

nose_x, nose_y, nose_trust = person1["pose_keypoints_2d"][:3] #リストの最初から3つの要素を取得
neck_x, neck_y, neck_trust = person1["pose_keypoints_2d"][3:6] #リストの3番目から6番目の要素を取得

# person1の結果を表示
print("Person 1")
print("Nose  X:", nose_x, "Y:", nose_y, "trust:", nose_trust)
print("Neck  X:", neck_x, "Y:", neck_y, "trust:", neck_trust)

# 0フレーム目の鼻と首の情報を取得 (Person 2)
nose_x, nose_y, nose_trust = person2["pose_keypoints_2d"][:3]
neck_x, neck_y, trust = person2["pose_keypoints_2d"][3:6]

# person2の結果
print("\nPerson 2")
print("Nose  X:", nose_x, "Y:", nose_y, "trust:", nose_trust)
print("Neck  X:", neck_x, "Y:", neck_y, "trust:", neck_trust)