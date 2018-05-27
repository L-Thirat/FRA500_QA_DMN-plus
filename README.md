# Dynamic Memory Networks in TensorFlow

DMN+ implementation in TensorFlow for question answering on the bAbI 10k dataset.

Structure and parameters from [Dynamic Memory Networks for Visual and Textual Question Answering](https://arxiv.org/abs/1603.01417) which is henceforth referred to as Xiong et al.

Adapted from Stanford's [cs224d](http://cs224d.stanford.edu/) assignment 2 starter code and using methods from [Dynamic Memory Networks in Theano](https://github.com/YerevaNN/Dynamic-memory-networks-in-Theano) for importing the Babi-10k dataset.

## Repository Contents
| file | description |
| --- | --- |
| `dmn_plus.py` | contains the DMN+ model |
| `dmn_train.py` | trains the model on a specified (-b) babi task|
| `dmn_test.py` | tests the model on a specified (-b) babi task |
| `babi_input.py` | prepares bAbI data for input into DMN |
| `attention_gru_cell.py` | contains a custom Attention GRU cell implementation |
| `fetch_babi_data.sh` | shell script to fetch bAbI tasks (from [DMNs in Theano](https://github.com/YerevaNN/Dynamic-memory-networks-in-Theano)) |

## Usage
Install [TensorFlow r1.4](https://www.tensorflow.org/install/)

Run the included shell script to fetch the data

	bash fetch_babi_data.sh

Use 'dmn_train.py' to train the DMN+ model contained in 'dmn_plus.py'

	python dmn_train.py --babi_task_id 2

Once training is finished, test the model on a specified task

	python dmn_test.py --babi_task_id 2

The l2 regularization constant can be set with -l2-loss (-l). All other parameters were specified by [Xiong et al](https://arxiv.org/abs/1603.01417) and can be found in the 'Config' class in 'dmn_plus.py'.

## Benchmarks
The TensorFlow DMN+ reaches close to state of the art performance on the 10k dataset with weak supervision (no supporting facts).

Each task was trained on separately with l2 = 0.001. As the paper suggests, 10 training runs were used for tasks 2, 3, 17 and 18 (configurable with --num-runs), where the weights which produce the lowest validation loss in any run are used for testing. 

The pre-trained weights which achieve these benchmarks are available in 'pretrained'.

I haven't yet had the time to fully optimize the l2 parameter which is not specified by the paper. My hypothesis is that fully optimizing l2 regularization would close the final significant performance gap between the TensorFlow DMN+ and original DMN+ on task 3. 

Below are the full results for each bAbI task (tasks where both implementations achieved 0 test error are omitted):

| Task ID | TensorFlow DMN+| Xiong et al DMN+ |
| :---: | :---: | :---: |
| 2 | 0.9 | 0.3 |
| 3 | 18.4 | 1.1 |
| 5 | 0.5 | 0.5 |
| 7 | 2.8 | 2.4 |
| 8 | 0.5 | 0.0 |
| 9 | 0.1 | 0.0 |
| 14 | 0.0 | 0.2 |
| 16 | 46.2 | 45.3 |
| 17 | 5.0 | 4.2 |
| 18 | 2.2 | 2.1 |

--Improve Solution--
DMN+ for Thai language
## All of my Source code are in https://github.com/few2005few/FRA500_QA_DMN-plus/tree/master/addition_fuse

## Data set
bAbI dataset (Task 1,2,5,6,10,12,14,17)
โดย dataset ที่เราแปลแล้วสามารถเข้าไปดูได้ใน https://github.com/few2005few/FRA500_QA_DMN-plus/tree/master/data_translate

## Translation
สำหรับการแปลงข้อมูล bAbI dataset จากภาษาอังกฤษเป็นภาษาไทย เราเลือกใช้ googletrans package ซึ่งทำหน้าที่ดึง API จาก Google Translation มาใช้ ซึ่งภายในโค้ดนี้เราได้เลือกโค้ดที่สามารถแก้เรื่องจำกัดลิมิตในการแปลได้ ทำให้เราสามารถแปลงข้อมูล bAbI dataset พร้อมๆกันได้ แต่เนื่องจากการจะแปลงข้อมูล bAbI dataset นั้นเราต้องการที่จะตัดข้อความในส่วนของคำถาม กับคำตอบให้แยกออกจากกัน เพื่อให้ google translate ตัวนี้ ไม่สับสนในการแปลข้อความซึ่งจัดการด้วย def loop_translate(ln) และมีการป้องกันการวนลูปทำใหม่กรณีที่อินเทอร์เน็ตใช้งานไม่ได้ หรือขัดข้องใน  def translate_txt(ln) นอกจากนี้ก็ยังมีการกำหนด Rule ต่างๆเพื่อให้การแปลมีความถูกต้องแม่นยำมากขึ้นใน get_babi_raw(id, test_id,mode_f)
# text_translate_2fact.py
This file is use to convert data set bAbI in English to Thai
สามารถเลือก data set ที่ต้องการจะรันด้วยการเปลี่ยน parameter ในบรรทัดสุดท้าย
>> get_babi_raw("3","3","train")
โดยที่พารามิเตอร์ตัวแรก คือ training set
ตัวที่สอง คือ test set
ตัวที่สาม คือ ชุดข้อมูลในการรัน ("train" / "test")
โดยเอาท์พุทคือไฟล์ใหม่ที่เป็น data set bAbI ภาษาไทย

## Word segmentation
เนื่องจากการแปลภาษาที่ได้จาก google translate นั้นจะได้ในรูปแบบประโยค ซึ่งทำให้เราจำเป็นต้องจัดการปัญหาในการตัดคำ ซึ่งเราได้เลือก package pythainlp มาใช้
https://medium.com/@rithikied/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%95%E0%B8%B1%E0%B8%94%E0%B8%84%E0%B8%B3%E0%B9%84%E0%B8%97%E0%B8%A2-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-python-307120e7ebf2
# Package pythainlp
สำหรับแพเกจนี้เราสามารถเลือกได้ว่าจะใช้อัลกอลิทึมอะไรในการตัดคำ ซึ่งประกอบด้วย
icu — engine ตัวดั้งเดิมของ PyThaiNLP (ความแม่นยำต่ำ) และเป็นค่าเริ่มต้น
dict — เป็นการตัดคำโดยใช้พจานุกรมจาก thaiword.txt ใน corpus (ความแม่นยำปานกลาง) จะคืนค่า False หากข้อความนั้นไม่สามารถตัดคำได้
longest-matching ใช้ Longest matching ในการตัดคำ
mm — ใช้ Maximum Matching algorithm ในการตัดคำภาษาไทย — API ชุดเก่า
newmm — ใช้ Maximum Matching algorithm ในการตัดคำภาษาไทย
pylexto ใช้ LexTo ในการตัดคำ โดยเป็น Longest matching
deepcut ใช้ deepcut จาก https://github.com/rkcosmos/deepcut ในการตัดคำภาษาไทย
wordcutpy ใช้ wordcutpy (https://github.com/veer66/wordcutpy) ในการตัดคำ
** โดยเราได้เลือกใช้อัลกอลิทึม Maximum Matching algorithm ในการตัดคำ ซึ่งได้อธิบาการทำงานของอัลกอลิทึมไว้ใน Project report

## Improvement experimental in Project report (Google classroom)
# Experiment 1-2: 
ในการทดลองที่ 1-2 เราอ้างอิงตาม package DMN+ เพียงแต่ทำการทดลองสองรอบ คือ train-test ด้วยภาษาอังกฤษ และภาษาไทยตามลำดับเพื่อเปรียบเทียบการทดลอง
python dmn_train.py --babi_task_id 2
python dmn_test.py --babi_task_id 2
โดยเราสามารถปรับ จำนวนรอบการ train ซึ่งอยู่ใน Experiment 1 ได้ที่ไฟล์ dmn_plut.py line 24>> max_epochs = 30

# Experiment 3: re_data.py
เราใช้ไฟล์นี้ในการแปลงข้อมูลภาษาไทยเช่น ตัดคำสร้อย เปลี่ยนชื่อคน และชื่อสถานที่ ที่อยู่ใน test set ของ dataset bAbI ให้เป็นคำใหม่ที่ไม่เคยปรากฎอยู่ใน  training set เพื่อทดสอบว่าโมเดลจะสามารถทำงานได้ดีหรือไม่ภายใต้เงื่อนไขนี้ เพราะว่าในความเป็นจริงแล้วข้อมูลที่เกิดจาก user นั้นอาจมีคำใหม่ที่ไม่เคยพบมาก่อนในตอนที่ train
ดังนั้นเราจึงใช้ไฟล์นี้ในการแปลงข้อมูลเหล่านั้นโดยการเลือก comment ในหัวข้อที่เราต้องการ
- ตัดคำสร้อย line 109-134
- แปลงชื่อคน line 100-107
- แปลงสรถานที่ line 136-150
จากนั้นจึงเลือก dataset ที่เราต้องการในบรรทัดสุดท้าย (get_babi_raw("10","10","test"))

# Experiment 4: dup_data.py
สำหรับการทดลองนี้เราต้องการที่จะเพิ่มประสิทธิภาพในปัญหาจากการทดลองที่ 3 ให้ดีขึ้น ด้วยการเพิ่มชื่อคนที่ปรากฎใน test set ลงใน training set เพื่อให้ระบบได้เรียน word vector ที่เกิดขึ้นใน test set ทั้งหมด โดยการคัดลอกไฟล์ (dupplicate) bAbI dataset ด้วยชื่อคนต่างๆที่เกิดขึ้นตาม test set ทุกกรณี จากนั้นำทุกไฟล์ที่ได้มา concatenate  เพื่อสร้างไฟล์ trainning set ที่คลุมรายชื่อที่เราแก้ไขใน test set มากขึ้น 
จากนั้นจึงเลือก dataset ที่เราต้องการในบรรทัดสุดท้าย (get_babi_raw("10","10","train",new_dup_seq))
โดยที่ new_dup_seq เป็น list ของรายชื่อคนที่ปรากฎใน test set
