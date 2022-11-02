from .dnn import LSTM, CNN1D
from .ml import SVM, MLP

def make(x_train, x_test, y_train, y_test, config, n_feats: int):
    """
    创建模型

    Args:
        config: 配置项
        n_feats (int): 特征数量
    """
    if config.model == 'svm':
        model = SVM.make(params=config.params)
    elif config.model == 'mlp':
        model = MLP.make(params=config.params)
    elif config.model == 'LSTM':
        model = LSTM.make(
            x_train = x_train, 
            x_test = x_test, 
            y_train = y_train, 
            y_test = y_test,
            input_shape = n_feats,
            rnn_size = config.rnn_size,
            hidden_size = config.hidden_size,
            dropout = config.dropout,
            n_classes = len(config.class_labels),
            # lr = config.lr,
            epochs = config.epochs,
            checkpoint_path = config.checkpoint_path,
            checkpoint_name = config.checkpoint_name
        )
    elif config.model == 'cnn1d':
        model = CNN1D.make(
            input_shape = n_feats,
            n_kernels = config.n_kernels,
            kernel_sizes = config.kernel_sizes,
            hidden_size = config.hidden_size,
            dropout = config.dropout,
            n_classes = len(config.class_labels),
            lr = config.lr
        )

    return model


_MODELS = {
    'cnn1d': CNN1D,
    'LSTM': LSTM,
    'mlp': MLP,
    'svm': SVM
}

def load(config):
    return _MODELS[config.model].load(
        path = config.checkpoint_path,
        name = config.checkpoint_name
    )
