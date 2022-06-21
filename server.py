from flask import Flask
from flask import request, jsonify
import json
import random
import copy
import pprint

class Solution:
    def defect_concoct(self, formated: list) -> str:
        results = []
        template = {
            "exception_info": 'null',     # 检测期间发生的异常，是个字符串；无异常时显示 null
            "imaging": 0,                 # 图片ID，和输入图片的 imaging 变量一致
            "product": 0,                 # 产品名称，和输入图片的 product 变量一致
            "defects": [],                # 产品缺陷
            "debug_info": {}              # 算法 debug 信息，内容待定
        }
 
        for img in formated:
            template_new = copy.deepcopy(template)
            flag = random.choice([True] + [False]*9)  #百分之10概率异常
            template_new['imaging'] = img['imaging']
            template_new['product'] = img['product']
            if flag:
                template_new['exception_info'] = 'abnormal'
                results.append(template_new)
                continue
            random_num = random.randint(0, len(defect_classes))
            template_new['defects'] = self.generate_defect(img['image_w'], img['image_h'], random_num)
            results.append(template_new)
        return results

    def generate_defect(self,image_w: int, image_h: int, random_num: int) -> list:
        results = []
        if random_num == 0:
            return results
        template = {
                "defect_type": None,   # 缺陷类型（所有缺陷类别的集合待定）
                "defect_x": 0,              # 缺陷左上角x轴坐标
                "defect_y": 0,             # 缺陷左上角y轴坐标
                "defect_w": 0,             # 缺陷宽度
                "defect_h": 0,              # 缺陷长度
                "attributes": {}          # 缺陷特征，内容待定
                }
        for defect in random.sample(defect_classes, random_num):
            template_new = copy.deepcopy(template)
            template_new["defect_type"] = defect
            template_new['defect_x'] = random.randint(1, image_w - 1)
            template_new['defect_y'] = random.randint(1, image_h - 1)
            template_new['defect_w'] = random.randint(1, image_w - template_new['defect_x'])
            template_new['defect_h'] = random.randint(1, image_h - template_new['defect_y'])
            results.append(template_new)  
        return results

app = Flask(__name__)

@app.route('/infer/', methods=['POST','GET'])
def http_infer():
    if request.method == 'POST':
        input_string = request.headers['input_string']
        inputs = json.loads(input_string) 
        solution = Solution()
        final = solution.defect_concoct(inputs) 
        return jsonify(final)
    else:
        input_string = request.headers['input_string']
        inputs = json.loads(input_string)
        solution = Solution()
        final = solution.defect_concoct(inputs) 
        return jsonify(final)
    
if __name__ == '__main__':
    defect_classes = ['blowhole','stoma','shrinkage','scab','coldshut','fissure','starving'] 
    app.run(host='127.0.0.1',port=3700)