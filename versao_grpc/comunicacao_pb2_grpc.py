# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import comunicacao_pb2 as comunicacao__pb2


class ComunicarStub(object):
    """Definiçao do Serviço de troca
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/comunicacao.Comunicar/Login',
                request_serializer=comunicacao__pb2.LoginRequest.SerializeToString,
                response_deserializer=comunicacao__pb2.LoginReply.FromString,
                )
        self.CadastroUsuario = channel.unary_unary(
                '/comunicacao.Comunicar/CadastroUsuario',
                request_serializer=comunicacao__pb2.LoginRequest.SerializeToString,
                response_deserializer=comunicacao__pb2.LoginReply.FromString,
                )
        self.ListagemDeitensTroca = channel.unary_unary(
                '/comunicacao.Comunicar/ListagemDeitensTroca',
                request_serializer=comunicacao__pb2.Vazia.SerializeToString,
                response_deserializer=comunicacao__pb2.ListaCervejaBar.FromString,
                )
        self.ListagemDeitensGeladeira = channel.unary_unary(
                '/comunicacao.Comunicar/ListagemDeitensGeladeira',
                request_serializer=comunicacao__pb2.ListaGeladeiraRequest.SerializeToString,
                response_deserializer=comunicacao__pb2.ListaCervejaBar.FromString,
                )
        self.ListagemTrocasPendentes = channel.unary_unary(
                '/comunicacao.Comunicar/ListagemTrocasPendentes',
                request_serializer=comunicacao__pb2.ListaTrocaRequest.SerializeToString,
                response_deserializer=comunicacao__pb2.ListaTrocas.FromString,
                )
        self.CadastroCerveja = channel.unary_unary(
                '/comunicacao.Comunicar/CadastroCerveja',
                request_serializer=comunicacao__pb2.CervejaCadastro.SerializeToString,
                response_deserializer=comunicacao__pb2.CadastroReply.FromString,
                )
        self.TrocarCerveja = channel.unary_unary(
                '/comunicacao.Comunicar/TrocarCerveja',
                request_serializer=comunicacao__pb2.TrocaRequest.SerializeToString,
                response_deserializer=comunicacao__pb2.TrocaReply.FromString,
                )


class ComunicarServicer(object):
    """Definiçao do Serviço de troca
    """

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CadastroUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListagemDeitensTroca(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListagemDeitensGeladeira(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListagemTrocasPendentes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CadastroCerveja(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrocarCerveja(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComunicarServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=comunicacao__pb2.LoginRequest.FromString,
                    response_serializer=comunicacao__pb2.LoginReply.SerializeToString,
            ),
            'CadastroUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.CadastroUsuario,
                    request_deserializer=comunicacao__pb2.LoginRequest.FromString,
                    response_serializer=comunicacao__pb2.LoginReply.SerializeToString,
            ),
            'ListagemDeitensTroca': grpc.unary_unary_rpc_method_handler(
                    servicer.ListagemDeitensTroca,
                    request_deserializer=comunicacao__pb2.Vazia.FromString,
                    response_serializer=comunicacao__pb2.ListaCervejaBar.SerializeToString,
            ),
            'ListagemDeitensGeladeira': grpc.unary_unary_rpc_method_handler(
                    servicer.ListagemDeitensGeladeira,
                    request_deserializer=comunicacao__pb2.ListaGeladeiraRequest.FromString,
                    response_serializer=comunicacao__pb2.ListaCervejaBar.SerializeToString,
            ),
            'ListagemTrocasPendentes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListagemTrocasPendentes,
                    request_deserializer=comunicacao__pb2.ListaTrocaRequest.FromString,
                    response_serializer=comunicacao__pb2.ListaTrocas.SerializeToString,
            ),
            'CadastroCerveja': grpc.unary_unary_rpc_method_handler(
                    servicer.CadastroCerveja,
                    request_deserializer=comunicacao__pb2.CervejaCadastro.FromString,
                    response_serializer=comunicacao__pb2.CadastroReply.SerializeToString,
            ),
            'TrocarCerveja': grpc.unary_unary_rpc_method_handler(
                    servicer.TrocarCerveja,
                    request_deserializer=comunicacao__pb2.TrocaRequest.FromString,
                    response_serializer=comunicacao__pb2.TrocaReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'comunicacao.Comunicar', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Comunicar(object):
    """Definiçao do Serviço de troca
    """

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comunicacao.Comunicar/Login',
            comunicacao__pb2.LoginRequest.SerializeToString,
            comunicacao__pb2.LoginReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CadastroUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comunicacao.Comunicar/CadastroUsuario',
            comunicacao__pb2.LoginRequest.SerializeToString,
            comunicacao__pb2.LoginReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListagemDeitensTroca(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comunicacao.Comunicar/ListagemDeitensTroca',
            comunicacao__pb2.Vazia.SerializeToString,
            comunicacao__pb2.ListaCervejaBar.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListagemDeitensGeladeira(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comunicacao.Comunicar/ListagemDeitensGeladeira',
            comunicacao__pb2.ListaGeladeiraRequest.SerializeToString,
            comunicacao__pb2.ListaCervejaBar.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListagemTrocasPendentes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comunicacao.Comunicar/ListagemTrocasPendentes',
            comunicacao__pb2.ListaTrocaRequest.SerializeToString,
            comunicacao__pb2.ListaTrocas.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CadastroCerveja(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comunicacao.Comunicar/CadastroCerveja',
            comunicacao__pb2.CervejaCadastro.SerializeToString,
            comunicacao__pb2.CadastroReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrocarCerveja(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/comunicacao.Comunicar/TrocarCerveja',
            comunicacao__pb2.TrocaRequest.SerializeToString,
            comunicacao__pb2.TrocaReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
