import grpc
import calculator_pb2
import calculator_pb2_grpc

# Step1: Create a Channel
channel = grpc.insecure_channel('localhost:80')

# Step2: Create a Stub
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Step3: call API
number = calculator_pb2.RequestNumber(val=16)
response = stub.SquareRoot(number)
print(response.val)