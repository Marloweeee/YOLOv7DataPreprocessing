# YOLO数据预处理丐版脚本

一般来说就是从xml、json或者txt文件中读取bbox信息并进行归一化，使其符合YOLO的数据标准，当前脚本仅仅涉及提取txt中bbox信息，xml、json之前写过有时间找找补充上

## 库依赖：

主要是xywh归一化过程中要使用image的size信息，所以需要借助opencv读取image的size，当然使用PIL.Image也是可以的，这里不赘述。

```python
pip install opencv-python
```

## 文件路径

```python
YOLOv7DataPreprocessing
	|-annos2yolo.py
	|-genPath.py
	|-scanDataAmount.py
	|-data
		|-train
			|-iamges
			|-labels
		|-val
			|-iamges
			|-labels
		|-test
			|-images
			|-labels
```

