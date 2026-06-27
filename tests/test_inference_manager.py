import pytest

from newface import content_analyser, state_manager


@pytest.fixture(scope = 'module', autouse = True)
def before_all() -> None:
	state_manager.init_item('execution_device_ids', [ 0 ])
	state_manager.init_item('execution_providers', [ 'cpu' ])
	state_manager.init_item('download_providers', [ 'github' ])
	assert content_analyser.pre_check() is True


def test_content_analyser_is_disabled() -> None:
	model_hash_set, model_source_set = content_analyser.collect_model_downloads()

	assert model_hash_set == {}
	assert model_source_set == {}
	assert content_analyser.get_inference_pool() == {}
