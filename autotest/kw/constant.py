import os

# 测试用例数据存放目录
TEST_CASE_DATA_DIR = os.getcwd() + "/testcase/"

# 测试套件文件路径
SUITE_FILE_PATH = TEST_CASE_DATA_DIR + "suite.xlsx"

# 用例和步骤执行结果
PASS = "PASS"
FAIL = "FAIL"
SKIP = "SKIP"

print(TEST_CASE_DATA_DIR)
print(SUITE_FILE_PATH)
