import sys
import os

if __name__ == '__main__':
    from concurrent import futures
    import grpc
    from weather_analyzer_pb2_grpc.weather_pb2_grpc import AuthServiceServicer
    from weather_analyzer_pb2_grpc.weather_pb2_grpc import AuthServiceStub
    from pyflask import app

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    AuthServiceServicer().add_to_server(server)
    server.add_insecure_port('[::]:50052')  # Choose a port for gRPC server
    server.start()
    app.run(port=8000)  # Start Flask app on port 8000
