# Changelog

## 0.3.0-alpha.1 (2025-08-22)

Full Changelog: [v0.2.18-alpha.3...v0.3.0-alpha.1](https://github.com/llamastack/llama-stack-client-python/compare/v0.2.18-alpha.3...v0.3.0-alpha.1)

### Features

* **api:** fix completion response breakage perhaps? ([f3b87fb](https://github.com/llamastack/llama-stack-client-python/commit/f3b87fb8922e781745aa55e2cfb8a421f769c8b1))


### Chores

* sync repo ([7501b6e](https://github.com/llamastack/llama-stack-client-python/commit/7501b6e151771176d825bff9c2e85c40d221a705))

## 0.2.18-alpha.3 (2025-08-14)

Full Changelog: [v0.2.18-alpha.2...v0.2.18-alpha.3](https://github.com/llamastack/llama-stack-client-python/compare/v0.2.18-alpha.2...v0.2.18-alpha.3)

### Features

* `llama-stack-client providers inspect PROVIDER_ID` ([#181](https://github.com/llamastack/llama-stack-client-python/issues/181)) ([6d18aae](https://github.com/llamastack/llama-stack-client-python/commit/6d18aae31ce739b1a37a72b880aa8a60f890df72))
* add client-side utility for getting OAuth tokens simply ([#230](https://github.com/llamastack/llama-stack-client-python/issues/230)) ([91156dc](https://github.com/llamastack/llama-stack-client-python/commit/91156dca28567352c5f6be75d55327ef2b49ff19))
* add client.chat.completions.create() and client.completions.create() ([#226](https://github.com/llamastack/llama-stack-client-python/issues/226)) ([ee0e65e](https://github.com/llamastack/llama-stack-client-python/commit/ee0e65e89dba13431cc3b9abdbebaa9525a5fbfb))
* Add llama-stack-client datasets unregister command ([#222](https://github.com/llamastack/llama-stack-client-python/issues/222)) ([38cd91c](https://github.com/llamastack/llama-stack-client-python/commit/38cd91c9e396f2be0bec1ee96a19771582ba6f17))
* add support for chat sessions ([#167](https://github.com/llamastack/llama-stack-client-python/issues/167)) ([ce3b30f](https://github.com/llamastack/llama-stack-client-python/commit/ce3b30f83eb122cc200c441ddad5e173e02e5adb))
* add type hints to event logger util ([#140](https://github.com/llamastack/llama-stack-client-python/issues/140)) ([26f3c33](https://github.com/llamastack/llama-stack-client-python/commit/26f3c33cd0f81b809afa514b9a8ca63fa64643ca))
* add updated batch inference types ([#220](https://github.com/llamastack/llama-stack-client-python/issues/220)) ([ddb93ca](https://github.com/llamastack/llama-stack-client-python/commit/ddb93ca206d97c82c51a0efed5985a7396fcdf3c))
* add weighted_average aggregation function support ([#208](https://github.com/llamastack/llama-stack-client-python/issues/208)) ([b62ac6c](https://github.com/llamastack/llama-stack-client-python/commit/b62ac6cf2f2f20e248cbbce6684cef50f150cac0))
* **agent:** support multiple tool calls ([#192](https://github.com/llamastack/llama-stack-client-python/issues/192)) ([43ea2f6](https://github.com/llamastack/llama-stack-client-python/commit/43ea2f6d741b26181db1d7ba0912c17a9ed1ca74))
* **agent:** support plain function as client_tool ([#187](https://github.com/llamastack/llama-stack-client-python/issues/187)) ([2ec8044](https://github.com/llamastack/llama-stack-client-python/commit/2ec8044356b5d6285948ae22da007899f6148408))
* **api:** update via SDK Studio ([48fd19c](https://github.com/llamastack/llama-stack-client-python/commit/48fd19caff46f4ea58cdcfb402e056ccadd096b8))
* async agent wrapper ([#169](https://github.com/llamastack/llama-stack-client-python/issues/169)) ([fc9907c](https://github.com/llamastack/llama-stack-client-python/commit/fc9907c781dc406756c20d8a1829343eac0c31c0))
* autogen llama-stack-client CLI reference doc ([#190](https://github.com/llamastack/llama-stack-client-python/issues/190)) ([e7b19a5](https://github.com/llamastack/llama-stack-client-python/commit/e7b19a505cc06c28846e85bb5b8524632bdef4d6))
* client.responses.create() and client.responses.retrieve() ([#227](https://github.com/llamastack/llama-stack-client-python/issues/227)) ([fba5102](https://github.com/llamastack/llama-stack-client-python/commit/fba5102d03f85627025f4589216651d135841d5a))
* datasets api updates ([#203](https://github.com/llamastack/llama-stack-client-python/issues/203)) ([b664564](https://github.com/llamastack/llama-stack-client-python/commit/b664564fe1c4771a7872286d0c2ac96c47816939))
* enable_persist: sync updates from stainless branch: yanxi0830/dev ([#145](https://github.com/llamastack/llama-stack-client-python/issues/145)) ([59a02f0](https://github.com/llamastack/llama-stack-client-python/commit/59a02f071b14cb6627c929c4d396a3d996219c78))
* new Agent API ([#178](https://github.com/llamastack/llama-stack-client-python/issues/178)) ([c2f73b1](https://github.com/llamastack/llama-stack-client-python/commit/c2f73b11301c6c4a87e58ded9055fd49b1626b47))
* support client tool output metadata ([#180](https://github.com/llamastack/llama-stack-client-python/issues/180)) ([8e4fd56](https://github.com/llamastack/llama-stack-client-python/commit/8e4fd56a318a2806e81679877d703f6270fbcbfe))
* Sync updates from stainless branch: ehhuang/dev ([#149](https://github.com/llamastack/llama-stack-client-python/issues/149)) ([367da69](https://github.com/llamastack/llama-stack-client-python/commit/367da690dabee8a34039499f8e151cc8f97ca91b))
* unify max infer iters with server/client tools ([#173](https://github.com/llamastack/llama-stack-client-python/issues/173)) ([548f2de](https://github.com/llamastack/llama-stack-client-python/commit/548f2dee5019b7510d17025f11adbf61431f505e))
* update react with new agent api ([#189](https://github.com/llamastack/llama-stack-client-python/issues/189)) ([ac9d1e2](https://github.com/llamastack/llama-stack-client-python/commit/ac9d1e2166c88d2445fbbf08e30886fcec6048df))


### Bug Fixes

* `llama-stack-client provider inspect` should use retrieve ([#202](https://github.com/llamastack/llama-stack-client-python/issues/202)) ([e33b5bf](https://github.com/llamastack/llama-stack-client-python/commit/e33b5bfbc89c93031434720cf7265f9bc83f2a39))
* accept extra_headers in agent.create_turn and pass them faithfully ([#228](https://github.com/llamastack/llama-stack-client-python/issues/228)) ([e72d9e8](https://github.com/llamastack/llama-stack-client-python/commit/e72d9e8eb590facd693938a93a7a782e45d15b6d))
* added uv.lock ([546e0df](https://github.com/llamastack/llama-stack-client-python/commit/546e0df348b648651da94989053c52f4cc43cdc4))
* **agent:** better error handling ([#207](https://github.com/llamastack/llama-stack-client-python/issues/207)) ([5746f91](https://github.com/llamastack/llama-stack-client-python/commit/5746f918351f9021700f0a90edf6b78e74d58c82))
* **agent:** initialize toolgroups/client_tools ([#186](https://github.com/llamastack/llama-stack-client-python/issues/186)) ([458e207](https://github.com/llamastack/llama-stack-client-python/commit/458e20702b5aa8f435ac5ce114fee9252b751d25))
* broken .retrieve call using `identifier=` ([#135](https://github.com/llamastack/llama-stack-client-python/issues/135)) ([626805a](https://github.com/llamastack/llama-stack-client-python/commit/626805a74a19011d742a60187b1119aead153a94))
* bump to 0.2.1 ([edb6173](https://github.com/llamastack/llama-stack-client-python/commit/edb6173ec1f0da131e097a993d6f177a3655930d))
* bump version ([b6d45b8](https://github.com/llamastack/llama-stack-client-python/commit/b6d45b862ca846bed635d64816dc7de9d9433e61))
* bump version in another place ([7253433](https://github.com/llamastack/llama-stack-client-python/commit/7253433f6d7a41fe0812d26e4ce7183f922f2869))
* **cli:** align cli toolgroups register to the new arguments ([#231](https://github.com/llamastack/llama-stack-client-python/issues/231)) ([a87b6f7](https://github.com/llamastack/llama-stack-client-python/commit/a87b6f7b3fd07262bfbd4321652e51b901c75df5))
* correct toolgroups_id parameter name on unregister call ([#235](https://github.com/llamastack/llama-stack-client-python/issues/235)) ([1be7904](https://github.com/llamastack/llama-stack-client-python/commit/1be7904133630127c0a98ba4aed1241eee548c81))
* fix duplicate model get help text ([#188](https://github.com/llamastack/llama-stack-client-python/issues/188)) ([4bab07a](https://github.com/llamastack/llama-stack-client-python/commit/4bab07a683adee9a476ce926fe809dafe3cc27f0))
* llama-stack-client providers list ([#134](https://github.com/llamastack/llama-stack-client-python/issues/134)) ([930138a](https://github.com/llamastack/llama-stack-client-python/commit/930138a9013ee9157d14ee0606b24c5677bf4387))
* react agent ([#200](https://github.com/llamastack/llama-stack-client-python/issues/200)) ([b779979](https://github.com/llamastack/llama-stack-client-python/commit/b779979c40c638e835e5190e5877f57430c89d97))
* React Agent for non-llama models  ([#174](https://github.com/llamastack/llama-stack-client-python/issues/174)) ([ee5dd2b](https://github.com/llamastack/llama-stack-client-python/commit/ee5dd2b662ffdeb78b324dddd6884a4d0f1fd901))
* React agent should be able to work with provided config ([#146](https://github.com/llamastack/llama-stack-client-python/issues/146)) ([08ab5df](https://github.com/llamastack/llama-stack-client-python/commit/08ab5df583bb74dea9104950c190f6101eb19c95))
* react agent with custom tool parser n_iters ([#184](https://github.com/llamastack/llama-stack-client-python/issues/184)) ([aaff961](https://github.com/llamastack/llama-stack-client-python/commit/aaff9618601f1cded040e57e0d8067699e595208))
* remove the alpha suffix in run_benchmark.py ([#179](https://github.com/llamastack/llama-stack-client-python/issues/179)) ([638f7f2](https://github.com/llamastack/llama-stack-client-python/commit/638f7f29513cdb87b9bf0cf7bc269d2c576d37ba))
* update CONTRIBUTING.md to point to uv instead of rye ([3fbe0cd](https://github.com/llamastack/llama-stack-client-python/commit/3fbe0cdd6a8e935732ddc513b0a6af01623a6999))
* update uv lock ([cc072c8](https://github.com/llamastack/llama-stack-client-python/commit/cc072c81b59c26f21eaba6ee0a7d56fc61c0317a))
* validate endpoint url ([#196](https://github.com/llamastack/llama-stack-client-python/issues/196)) ([6fa8095](https://github.com/llamastack/llama-stack-client-python/commit/6fa8095428804a9cc348b403468cad64e4eeb38b))


### Chores

* api sync, deprecate allow_resume_turn + rename task_config-&gt;benchmark_config (Sync updates from stainless branch: yanxi0830/dev) ([#176](https://github.com/llamastack/llama-stack-client-python/issues/176)) ([96749af](https://github.com/llamastack/llama-stack-client-python/commit/96749af83891d47be1f8f46588be567db685cf12))
* AsyncAgent should use ToolResponse instead of ToolResponseMessage ([#197](https://github.com/llamastack/llama-stack-client-python/issues/197)) ([6191aa5](https://github.com/llamastack/llama-stack-client-python/commit/6191aa5cc38c4ef9be27452e04867b6ce8a703e2))
* **copy:** Copy changes over from llamastack/ org repository ([#255](https://github.com/llamastack/llama-stack-client-python/issues/255)) ([7ade969](https://github.com/llamastack/llama-stack-client-python/commit/7ade96987294cfd164d710befb15943fd8f8bb8b))
* deprecate eval task (Sync updates from stainless branch: main) ([#150](https://github.com/llamastack/llama-stack-client-python/issues/150)) ([39b1248](https://github.com/llamastack/llama-stack-client-python/commit/39b1248e3e1b0634e96db6bb4eac7d689e3a5a19))
* remove litellm type conversion ([#193](https://github.com/llamastack/llama-stack-client-python/issues/193)) ([ab3f844](https://github.com/llamastack/llama-stack-client-python/commit/ab3f844a8a7a8dc68723ed36120914fd01a18af2))
* sync repo ([099bfc6](https://github.com/llamastack/llama-stack-client-python/commit/099bfc66cdc115e857d5cfba675a090148619c92))
* Sync updates from stainless branch: ehhuang/dev ([#182](https://github.com/llamastack/llama-stack-client-python/issues/182)) ([e33aa4a](https://github.com/llamastack/llama-stack-client-python/commit/e33aa4a682fda23d708438a976dfe4dd5443a320))
* Sync updates from stainless branch: ehhuang/dev ([#199](https://github.com/llamastack/llama-stack-client-python/issues/199)) ([fa73d7d](https://github.com/llamastack/llama-stack-client-python/commit/fa73d7ddb72682d47464eca6b1476044e140a560))
* Sync updates from stainless branch: main ([#201](https://github.com/llamastack/llama-stack-client-python/issues/201)) ([f063f2d](https://github.com/llamastack/llama-stack-client-python/commit/f063f2d6126d2bd1f9a8dcf854a32ae7cd4be607))
* use rich to format logs ([#177](https://github.com/llamastack/llama-stack-client-python/issues/177)) ([303054b](https://github.com/llamastack/llama-stack-client-python/commit/303054b6a64e47dbdf7de93458433b71bb1ff59c))


### Refactors

* update react_agent to use tool_config ([#139](https://github.com/llamastack/llama-stack-client-python/issues/139)) ([b5dce10](https://github.com/llamastack/llama-stack-client-python/commit/b5dce10f0a621f8f8a0f893dba4d2acebd7e438b))


### Build System

* Bump version to 0.1.19 ([ccd52f8](https://github.com/llamastack/llama-stack-client-python/commit/ccd52f8bb298ecfd3ec06ae2d50ccaeebbfb3973))
* Bump version to 0.1.8 ([0144e85](https://github.com/llamastack/llama-stack-client-python/commit/0144e857c83afc807122b32f3f53775e87c027ac))
* Bump version to 0.1.9 ([7e00b78](https://github.com/llamastack/llama-stack-client-python/commit/7e00b784ee859aa04aa11955e3888e5167331dfe))
* Bump version to 0.2.10 ([05e41a6](https://github.com/llamastack/llama-stack-client-python/commit/05e41a6eb12053b850a3abc56bb35e3121042be2))
* Bump version to 0.2.11 ([d2e7537](https://github.com/llamastack/llama-stack-client-python/commit/d2e753751519cb9f0e09d255e875f60449ab30aa))
* Bump version to 0.2.12 ([e3d812e](https://github.com/llamastack/llama-stack-client-python/commit/e3d812ee3a85949e31e448e68c03534225b4ed07))
* Bump version to 0.2.13 ([b6c6c5e](https://github.com/llamastack/llama-stack-client-python/commit/b6c6c5ed7940bb625665d50f88ff7ea9d734e100))
* Bump version to 0.2.2 ([47f8fd5](https://github.com/llamastack/llama-stack-client-python/commit/47f8fd568634c9e2f7cd7d86f92f7c43cfc448cd))
* Bump version to 0.2.4 ([7e6f5fc](https://github.com/llamastack/llama-stack-client-python/commit/7e6f5fce18f23b807e52ac173251687c3b58979b))
* Bump version to 0.2.5 ([62bd127](https://github.com/llamastack/llama-stack-client-python/commit/62bd12799d8a4a0261d200d1c869e2be98c38770))
* Bump version to 0.2.6 ([3dd707f](https://github.com/llamastack/llama-stack-client-python/commit/3dd707fb84ba2ce56151cec9fb30918c651ccdd9))
* Bump version to 0.2.7 ([e39ba88](https://github.com/llamastack/llama-stack-client-python/commit/e39ba882f9d1f635f5e7398f623d7ceeae1b446f))
* Bump version to 0.2.8 ([645d219](https://github.com/llamastack/llama-stack-client-python/commit/645d2195c5af1c6f903cb93c293319d8f94c36cc))
* Bump version to 0.2.9 ([d360557](https://github.com/llamastack/llama-stack-client-python/commit/d36055741dd5c152c629dc28ec3b88b2c78f5336))

## 0.2.18-alpha.2 (2025-08-12)

Full Changelog: [v0.2.18-alpha.1...v0.2.18-alpha.2](https://github.com/llamastack/llama-stack-client-python/compare/v0.2.18-alpha.1...v0.2.18-alpha.2)

### Features

* **api:** update via SDK Studio ([e8e7433](https://github.com/llamastack/llama-stack-client-python/commit/e8e7433dab536ac6f03e72acfbf82505298fd44d))

## 0.2.18-alpha.1 (2025-08-12)

Full Changelog: [v0.2.18-alpha.1...v0.2.18-alpha.1](https://github.com/llamastack/llama-stack-client-python/compare/v0.2.18-alpha.1...v0.2.18-alpha.1)

### Features

* **api:** update via SDK Studio ([db99707](https://github.com/llamastack/llama-stack-client-python/commit/db9970745de255a3718edb6aee8360b55f58592e))

## 0.2.18-alpha.1 (2025-08-12)

Full Changelog: [v0.2.17...v0.2.18-alpha.1](https://github.com/llamastack/llama-stack-client-python/compare/v0.2.17...v0.2.18-alpha.1)

### Features

* **api:** update via SDK Studio ([8afae6c](https://github.com/llamastack/llama-stack-client-python/commit/8afae6c1e1a4614cc59db7ae511440693e0479a6))
* **api:** update via SDK Studio ([143a973](https://github.com/llamastack/llama-stack-client-python/commit/143a973ea9ff81da1d93c421af8c85dbd171ef3c))
* **api:** update via SDK Studio ([b8e32bb](https://github.com/llamastack/llama-stack-client-python/commit/b8e32bbbf68f8a75c956079119c6b65d7ac165e5))
* **api:** update via SDK Studio ([1a2c77d](https://github.com/llamastack/llama-stack-client-python/commit/1a2c77df732eb9d0c031e0ff7558176fbf754ad8))
* **api:** update via SDK Studio ([d66fb5f](https://github.com/llamastack/llama-stack-client-python/commit/d66fb5fe89acb66a55066d82b849bbf4d402db99))


### Chores

* **internal:** update comment in script ([8d599cd](https://github.com/llamastack/llama-stack-client-python/commit/8d599cd47f98f704f89c9bd979a55cc334895107))
* update @stainless-api/prism-cli to v5.15.0 ([5f8ae94](https://github.com/llamastack/llama-stack-client-python/commit/5f8ae94955bb3403c0abe89f2999c2d49af97b07))

## 0.2.17 (2025-08-06)

Full Changelog: [v0.2.15...v0.2.17](https://github.com/llamastack/llama-stack-client-python/compare/v0.2.15...v0.2.17)

### Features

* **api:** update via SDK Studio ([9c69353](https://github.com/llamastack/llama-stack-client-python/commit/9c693530330ad5e2bb427ccfeb154ac993601e05))
* **api:** update via SDK Studio ([5f90b04](https://github.com/llamastack/llama-stack-client-python/commit/5f90b04bd0b07cc20729551b88578ff322231723))
* **api:** update via SDK Studio ([6e26309](https://github.com/llamastack/llama-stack-client-python/commit/6e26309d14cb0b0a0b5d43b7cbab56528b878fd9))
* **api:** update via SDK Studio ([54ff3c4](https://github.com/llamastack/llama-stack-client-python/commit/54ff3c405af01ce068230990654b75d26967e745))
* **api:** update via SDK Studio ([a34c823](https://github.com/llamastack/llama-stack-client-python/commit/a34c8230f8a3f6f356c4f990f66bb02eda229819))
* **api:** update via SDK Studio ([f6b80ca](https://github.com/llamastack/llama-stack-client-python/commit/f6b80caaad58711957b7935f9b6833528ae3bd78))
* **api:** update via SDK Studio ([2a4296d](https://github.com/llamastack/llama-stack-client-python/commit/2a4296d3df60787b4fc3fe2812d06d6080b0d6db))
* **api:** update via SDK Studio ([07691ac](https://github.com/llamastack/llama-stack-client-python/commit/07691acac571ff68cd1ff90f9d60ac3e49b1e144))
* **api:** update via SDK Studio ([585f9ce](https://github.com/llamastack/llama-stack-client-python/commit/585f9ce929e0ac17775febb573fa109d9f3d07ac))
* **api:** update via SDK Studio ([6d609e3](https://github.com/llamastack/llama-stack-client-python/commit/6d609e3b9e31477fd540dff8c0ecb24bc9d524d1))
* **api:** update via SDK Studio ([3dbf2a4](https://github.com/llamastack/llama-stack-client-python/commit/3dbf2a4f205d7199cd4d92a7f3f6a2ee5723cb71))
* **api:** update via SDK Studio ([dd0ae96](https://github.com/llamastack/llama-stack-client-python/commit/dd0ae96300ce6d2940063a7b33c0948d250bbc5e))
* **api:** update via SDK Studio ([80a2969](https://github.com/llamastack/llama-stack-client-python/commit/80a296977917382fa42b0def0c6bf1a66be45780))
* **api:** update via SDK Studio ([748e6db](https://github.com/llamastack/llama-stack-client-python/commit/748e6db5002f1ec2c8880414b803d1cfc3ff95ea))
* **api:** update via SDK Studio ([b6fa2b1](https://github.com/llamastack/llama-stack-client-python/commit/b6fa2b194bc4d66adcc40b5cc07404c45a211cd3))
* **api:** update via SDK Studio ([e97f870](https://github.com/llamastack/llama-stack-client-python/commit/e97f870b037685af1e65d8d895a063ab2381dc81))
* **api:** update via SDK Studio ([489b54d](https://github.com/llamastack/llama-stack-client-python/commit/489b54d7acfee41874e2fa253578d3e95f6b111a))
* **api:** update via SDK Studio ([13cfa4a](https://github.com/llamastack/llama-stack-client-python/commit/13cfa4aa1f12b7369f1bc13c3dff8d4cea46a3f6))
* **api:** update via SDK Studio ([25c1e49](https://github.com/llamastack/llama-stack-client-python/commit/25c1e49f503e15649e0cdc18b0ac8dd00c2dff7e))
* **api:** update via SDK Studio ([4a54d61](https://github.com/llamastack/llama-stack-client-python/commit/4a54d613ee0a7ff7a561bc41db626aaea3c00096))
* **api:** update via SDK Studio ([ac4614a](https://github.com/llamastack/llama-stack-client-python/commit/ac4614a70aa632a7bc55037aa777f0ab40ea908b))
* **api:** update via SDK Studio ([a201e22](https://github.com/llamastack/llama-stack-client-python/commit/a201e22e2bad1b2290092784d4e2255eaaf73758))
* **client:** support file upload requests ([e84459f](https://github.com/llamastack/llama-stack-client-python/commit/e84459fc65a28e68ed185d6dba28b559e6882b99))
* **client:** support file upload requests ([6c73da7](https://github.com/llamastack/llama-stack-client-python/commit/6c73da7c97a558468296f1e8d6da5ba7ae9ea1c4))


### Bug Fixes

* **ci:** correct conditional ([d7c2ab8](https://github.com/llamastack/llama-stack-client-python/commit/d7c2ab87065aaade14a143113c90a0082ef35ee4))
* **ci:** correct conditional ([4368fbd](https://github.com/llamastack/llama-stack-client-python/commit/4368fbd1f733cfda7a2d4273f0c983e44be63fe1))
* **client:** don't send Content-Type header on GET requests ([d6a80a5](https://github.com/llamastack/llama-stack-client-python/commit/d6a80a5c38305c63494a9f8498e47ba0c0031295))
* **client:** don't send Content-Type header on GET requests ([c6e0026](https://github.com/llamastack/llama-stack-client-python/commit/c6e0026218d4fde46e23663b55384bdf417fbcbf))
* helptext for 'inspect version' and 'providers inspect' ([#8](https://github.com/llamastack/llama-stack-client-python/issues/8)) ([d79345e](https://github.com/llamastack/llama-stack-client-python/commit/d79345e42d6a3f3b828396b1ac00e2ecf196c0eb))
* kill requirements.txt ([a6bd44c](https://github.com/llamastack/llama-stack-client-python/commit/a6bd44c5bdb9415a8cacd53b552b8b43e341d91c))
* model register missing model-type and not accepting metadata ([#11](https://github.com/llamastack/llama-stack-client-python/issues/11)) ([f3f4515](https://github.com/llamastack/llama-stack-client-python/commit/f3f45155864379f227824d00f6febb1b46ed4839))
* **parsing:** correctly handle nested discriminated unions ([9f95130](https://github.com/llamastack/llama-stack-client-python/commit/9f95130b77729d2adcf906355ddef41d109999d0))
* **parsing:** correctly handle nested discriminated unions ([8b7e9ba](https://github.com/llamastack/llama-stack-client-python/commit/8b7e9ba42dbafb89d765f870d7874c86f47b2e7b))
* **parsing:** ignore empty metadata ([a8a398f](https://github.com/llamastack/llama-stack-client-python/commit/a8a398fb7ca67117d3b7663354a406d1432fd8fb))
* **parsing:** ignore empty metadata ([264f24c](https://github.com/llamastack/llama-stack-client-python/commit/264f24c9c564a0a5ea862418bfebb6c3cad01cf0))
* **parsing:** parse extra field types ([f981bdc](https://github.com/llamastack/llama-stack-client-python/commit/f981bdc927411cb3b69febd578d39299dac27670))
* **parsing:** parse extra field types ([d54c5db](https://github.com/llamastack/llama-stack-client-python/commit/d54c5db3df7b6e5dca66e8e7c855998c67d03250))
* pre-commit formatting ([a83b1c3](https://github.com/llamastack/llama-stack-client-python/commit/a83b1c36b8acff7d7f762d0eab9d832a3320bcce))
* update agent event logger ([#10](https://github.com/llamastack/llama-stack-client-python/issues/10)) ([0a10b70](https://github.com/llamastack/llama-stack-client-python/commit/0a10b70f91f28f533710433ae860789f2cb0f70f))


### Chores

* **ci:** change upload type ([7827103](https://github.com/llamastack/llama-stack-client-python/commit/78271038dcd35ea78fc2addf0676c4cdbea07a0e))
* **ci:** change upload type ([5febc13](https://github.com/llamastack/llama-stack-client-python/commit/5febc136956ce6ac5af8e638a6fa430a9d0f3dc3))
* **ci:** only run for pushes and fork pull requests ([03a7636](https://github.com/llamastack/llama-stack-client-python/commit/03a7636bce1974ef9be709cd6df395d687f0f22b))
* **ci:** only run for pushes and fork pull requests ([c05df66](https://github.com/llamastack/llama-stack-client-python/commit/c05df6620f31a4860e11c5b94b3d7bf85fc9d197))
* **ci:** only run for pushes and fork pull requests ([87c9d01](https://github.com/llamastack/llama-stack-client-python/commit/87c9d01fd4f8451882e1b936ba43375e20a56622))
* **ci:** only run for pushes and fork pull requests ([9d04993](https://github.com/llamastack/llama-stack-client-python/commit/9d04993f6cc133f6ea6ca943d14a59e9b309938a))
* **ci:** only run for pushes and fork pull requests ([4da7f49](https://github.com/llamastack/llama-stack-client-python/commit/4da7f495eb06d0cb386deeef3825c4876c64cbe2))
* **ci:** only run for pushes and fork pull requests ([8b37cd3](https://github.com/llamastack/llama-stack-client-python/commit/8b37cd35c06ba045c25be9f6777b854bd9d9dbf8))
* **ci:** only run for pushes and fork pull requests ([3f0a4b9](https://github.com/llamastack/llama-stack-client-python/commit/3f0a4b9ba82bd9db5ae9f854a2a775781eb75fd0))
* **ci:** only run for pushes and fork pull requests ([8a1efad](https://github.com/llamastack/llama-stack-client-python/commit/8a1efade982126d1742c912069321ce7bd267bd8))
* delete unused scripts based on rye ([dae6506](https://github.com/llamastack/llama-stack-client-python/commit/dae65069d31bc4d3e55c15f3f1848d00c35a75ce))
* **internal:** bump pinned h11 dep ([4a7073f](https://github.com/llamastack/llama-stack-client-python/commit/4a7073f0e60aea8a2b7ec6d72b31fc9554234ef0))
* **internal:** bump pinned h11 dep ([0568d6d](https://github.com/llamastack/llama-stack-client-python/commit/0568d6d078eab8f65ac191218d6467df9bfa7901))
* **internal:** codegen related update ([4d4afec](https://github.com/llamastack/llama-stack-client-python/commit/4d4afec936a1e6b2f0bf96a5508fb54620c894e4))
* **internal:** codegen related update ([7cd543f](https://github.com/llamastack/llama-stack-client-python/commit/7cd543f782490fe6ed5a90474114c1ef084a8b34))
* **internal:** codegen related update ([3165cad](https://github.com/llamastack/llama-stack-client-python/commit/3165cad3251782f4bfe529d9bdde1f18b5813fc0))
* **internal:** codegen related update ([c27a701](https://github.com/llamastack/llama-stack-client-python/commit/c27a7015e1627582e00de6c4f6cbc9df9da99c54))
* **internal:** codegen related update ([aa45ba3](https://github.com/llamastack/llama-stack-client-python/commit/aa45ba35f7107e6278c45134f6130ffaf99eb20e))
* **internal:** codegen related update ([5d6ccb5](https://github.com/llamastack/llama-stack-client-python/commit/5d6ccb56adf0cdeafd2d027ba2f897fd2f5c7070))
* **internal:** fix ruff target version ([c50a0e0](https://github.com/llamastack/llama-stack-client-python/commit/c50a0e0ee44f97ee1ac8ac2a9e80860ae7b71a37))
* **internal:** version bump ([5af7869](https://github.com/llamastack/llama-stack-client-python/commit/5af7869be75f6e577c57509c11e55a6dbbcdc4d8))
* **internal:** version bump ([148be8d](https://github.com/llamastack/llama-stack-client-python/commit/148be8d37f92a77e553edd599ad4a5981642b40c))
* **internal:** version bump ([86a0766](https://github.com/llamastack/llama-stack-client-python/commit/86a0766da6a2e282a2185b42530266aaa4c1a9ce))
* **internal:** version bump ([5d6cc6b](https://github.com/llamastack/llama-stack-client-python/commit/5d6cc6be97ca098140575e65803d3d51ddc1e9ea))
* **internal:** version bump ([cc7a519](https://github.com/llamastack/llama-stack-client-python/commit/cc7a51927110f8f4ef7309b9f6c92ace0434b24e))
* **internal:** version bump ([8f15ef0](https://github.com/llamastack/llama-stack-client-python/commit/8f15ef01b12c88af245e477362f86785586b697f))
* **internal:** version bump ([f52cb89](https://github.com/llamastack/llama-stack-client-python/commit/f52cb89e8a8d2e2b41155b6b5db2e700d85fcc29))
* **internal:** version bump ([2e1a629](https://github.com/llamastack/llama-stack-client-python/commit/2e1a629e8d24c37031d8d853ec5e3d9200952934))
* **internal:** version bump ([da26ed0](https://github.com/llamastack/llama-stack-client-python/commit/da26ed01f5ad7ff77d0b2166a0c282806a6d1aff))
* **internal:** version bump ([3727fa5](https://github.com/llamastack/llama-stack-client-python/commit/3727fa5703c3e6cfc38fc963650cee1af23c6d68))
* **internal:** version bump ([443ce02](https://github.com/llamastack/llama-stack-client-python/commit/443ce023733e06e1a83920727630ad4442aa2104))
* **internal:** version bump ([b2875ec](https://github.com/llamastack/llama-stack-client-python/commit/b2875ecbe69976ccaeeafb7b6216b711a0214edb))
* **internal:** version bump ([9a4320d](https://github.com/llamastack/llama-stack-client-python/commit/9a4320d7a4a81412a8657f23a9b8e3331770951a))
* **internal:** version bump ([39155e5](https://github.com/llamastack/llama-stack-client-python/commit/39155e53bff8e0255b5c62e7aa3e9b801c719f96))
* **internal:** version bump ([607c7be](https://github.com/llamastack/llama-stack-client-python/commit/607c7bea3d8e24d12069fa8a496380319badd71c))
* **internal:** version bump ([62901e7](https://github.com/llamastack/llama-stack-client-python/commit/62901e7b3bb26956f28b2443508d59ab6bc926b4))
* **internal:** version bump ([4132af9](https://github.com/llamastack/llama-stack-client-python/commit/4132af981fe9d59864c6f2d23258c893200355c1))
* **internal:** version bump ([e6ae920](https://github.com/llamastack/llama-stack-client-python/commit/e6ae920385cf6a92f1f0623428a61e0325521e67))
* **internal:** version bump ([96768dc](https://github.com/llamastack/llama-stack-client-python/commit/96768dc3db60936a960a9a46b9597df292a9e85e))
* **internal:** version bump ([74f7eda](https://github.com/llamastack/llama-stack-client-python/commit/74f7eda7bf4a5d024bdeaf36a0f228d610134530))
* **internal:** version bump ([d59862a](https://github.com/llamastack/llama-stack-client-python/commit/d59862a1bca2d31bf0f6cd0138bf2a1d804aad9d))
* **internal:** version bump ([ce98414](https://github.com/llamastack/llama-stack-client-python/commit/ce98414b294a451ac67b9fcee045f28ecce7b408))
* **internal:** version bump ([9746774](https://github.com/llamastack/llama-stack-client-python/commit/9746774316aed9a04b5ee161452df14e88f3e62c))
* **internal:** version bump ([6114dbf](https://github.com/llamastack/llama-stack-client-python/commit/6114dbf530354a56539a16a49a7c314bf643fca7))
* **internal:** version bump ([02c9953](https://github.com/llamastack/llama-stack-client-python/commit/02c9953a78c22d447d5a93b901a2684cce25ee3d))
* **internal:** version bump ([16f2953](https://github.com/llamastack/llama-stack-client-python/commit/16f2953d3292c3787e28f5178d1d149d6c808258))
* **internal:** version bump ([c32029b](https://github.com/llamastack/llama-stack-client-python/commit/c32029b26c4e10bba8378cbb61d6b2d7e6c3d10d))
* **internal:** version bump ([aef5dee](https://github.com/llamastack/llama-stack-client-python/commit/aef5dee81270b6372479fbeb2257d42f487dfcf3))
* **internal:** version bump ([590de6d](https://github.com/llamastack/llama-stack-client-python/commit/590de6d2ac748199b489c00fe8f79d9f8111a283))
* **internal:** version bump ([072269f](https://github.com/llamastack/llama-stack-client-python/commit/072269f0c2421313a1ba7a9feb372a72cc5f5f0f))
* **internal:** version bump ([eee6f0b](https://github.com/llamastack/llama-stack-client-python/commit/eee6f0b5cd146fc962d13da371e09e5abd66f05e))
* **internal:** version bump ([e6a964e](https://github.com/llamastack/llama-stack-client-python/commit/e6a964e9970e5d4bbd9f3bb9dae959ce6488b3bf))
* **package:** mark python 3.13 as supported ([2afc17b](https://github.com/llamastack/llama-stack-client-python/commit/2afc17ba76b498f6f0c975111bfd9456090d10b5))
* **package:** mark python 3.13 as supported ([d1a4e40](https://github.com/llamastack/llama-stack-client-python/commit/d1a4e40ba6a6d1b0ecf7b84cff55a79a6c00b925))
* **project:** add settings file for vscode ([405febd](https://github.com/llamastack/llama-stack-client-python/commit/405febd7158db4c129c854293a735c8c71712bc5))
* **project:** add settings file for vscode ([1dd3e53](https://github.com/llamastack/llama-stack-client-python/commit/1dd3e5310f668e81d246f929e2bd6b216a4ac9ad))
* **readme:** fix version rendering on pypi ([ca89c7f](https://github.com/llamastack/llama-stack-client-python/commit/ca89c7fb2e09ef52565f7de34068b3b4bbb575dc))
* **readme:** fix version rendering on pypi ([193fb64](https://github.com/llamastack/llama-stack-client-python/commit/193fb64864ce57e9a488d9ee874cededeaad1eae))
* update SDK settings ([2d422f9](https://github.com/llamastack/llama-stack-client-python/commit/2d422f92ee95364dc67c6557beafccde42ea11eb))
* update SDK settings ([59b933c](https://github.com/llamastack/llama-stack-client-python/commit/59b933ca39e08b9a36669995b3b5424231df84f5))
* update version ([10ef53e](https://github.com/llamastack/llama-stack-client-python/commit/10ef53e74dbdd72a8dd829957820e61522fbe6ad))


### Build System

* Bump version to 0.2.14 ([745a94e](https://github.com/llamastack/llama-stack-client-python/commit/745a94e1d2875c8e7b4fac5b1676b890aebf4915))
* Bump version to 0.2.15 ([8700dc6](https://github.com/llamastack/llama-stack-client-python/commit/8700dc6ed9411d436422ee94af2702f10a96b49e))
* Bump version to 0.2.15 ([4692024](https://github.com/llamastack/llama-stack-client-python/commit/46920241be5f8b921bbba367e65a7afa3aefd612))
* Bump version to 0.2.16 ([6ce9b84](https://github.com/llamastack/llama-stack-client-python/commit/6ce9b84007967702f6844679604e1b812df864e4))
* Bump version to 0.2.17 ([69f67ef](https://github.com/llamastack/llama-stack-client-python/commit/69f67ef77c9ca6ffc089a6d24261272aa2fee36f))

## 0.1.0-alpha.4 (2025-06-27)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/llamastack/llama-stack-client-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([4333cb0](https://github.com/llamastack/llama-stack-client-python/commit/4333cb0307fd99654e53e8f87b3b2951be027b44))


### Bug Fixes

* **ci:** update pyproject.toml to use uv and remove broken CI ([#5](https://github.com/llamastack/llama-stack-client-python/issues/5)) ([7bc925c](https://github.com/llamastack/llama-stack-client-python/commit/7bc925c00401799d8f3345a4873f1b0028cb45ea))


### Chores

* **internal:** version bump ([867ea24](https://github.com/llamastack/llama-stack-client-python/commit/867ea24344fd71fc9787807a47144af5e3de82f8))

## 0.1.0-alpha.3 (2025-06-27)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/llamastack/llama-stack-client-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([e87f225](https://github.com/llamastack/llama-stack-client-python/commit/e87f2257b00a287dd34dc95f4d39661728075891))
* make custom code changes ([#3](https://github.com/llamastack/llama-stack-client-python/issues/3)) ([83fa371](https://github.com/llamastack/llama-stack-client-python/commit/83fa37124133aab73bf2bbbdcd39338b9a192475))

## 0.1.0-alpha.2 (2025-06-27)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/llamastack/llama-stack-client-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([f568f65](https://github.com/llamastack/llama-stack-client-python/commit/f568f6508002eff7eae4a6b0a1cc13aba6fab98e))

## 0.1.0-alpha.1 (2025-06-27)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/llamastack/llama-stack-client-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **client:** add follow_redirects request option ([a77a9ee](https://github.com/llamastack/llama-stack-client-python/commit/a77a9eed9038782ba6b93ce0d3147ee4a6b8a3b7))
* **client:** add support for aiohttp ([d78982b](https://github.com/llamastack/llama-stack-client-python/commit/d78982b197c5e0a0fb67afcb44e9644fd8d931be))


### Bug Fixes

* **ci:** release-doctor — report correct token name ([6f3a4e2](https://github.com/llamastack/llama-stack-client-python/commit/6f3a4e24d8b357d7dc01adb0d9f736989fa9517d))
* **client:** correctly parse binary response | stream ([85d6bbd](https://github.com/llamastack/llama-stack-client-python/commit/85d6bbd97efac7509cbff0bb2d461a80d09b5e61))
* **package:** support direct resource imports ([a862d55](https://github.com/llamastack/llama-stack-client-python/commit/a862d551553aac41573306ce39480e1eb16ea3d3))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([347a4bf](https://github.com/llamastack/llama-stack-client-python/commit/347a4bffa920f5727a4c02eba18bd207001698b5))


### Chores

* change publish docs url ([fdd7a07](https://github.com/llamastack/llama-stack-client-python/commit/fdd7a075564ac206e91b2d06bf130c4de9473838))
* **ci:** enable for pull requests ([c9b6347](https://github.com/llamastack/llama-stack-client-python/commit/c9b6347f084acb1566b8e8283cf0bcfde7f6562c))
* **ci:** fix installation instructions ([40d9854](https://github.com/llamastack/llama-stack-client-python/commit/40d9854bd2630a471f1ca93d249e4d44b73fa864))
* **ci:** upload sdks to package manager ([2d2282b](https://github.com/llamastack/llama-stack-client-python/commit/2d2282bb49d58daef1f32fa0f1e5a356abf8df0d))
* **docs:** grammar improvements ([6f57b13](https://github.com/llamastack/llama-stack-client-python/commit/6f57b1363367de7ed5035fd1d6ba1a071eee67ba))
* **docs:** remove reference to rye shell ([bcf315a](https://github.com/llamastack/llama-stack-client-python/commit/bcf315ae00c458f89dfa3684bcc7abdb732b6c5f))
* **docs:** remove unnecessary param examples ([60ec829](https://github.com/llamastack/llama-stack-client-python/commit/60ec829e809156217cf2f911b3cac6b23a06baad))
* **internal:** avoid errors for isinstance checks on proxies ([758a188](https://github.com/llamastack/llama-stack-client-python/commit/758a188dbfaa284a13b70816689c99917a05d16c))
* **internal:** codegen related update ([ab9f05c](https://github.com/llamastack/llama-stack-client-python/commit/ab9f05cc1da5b21afceacdf9c8eb54b6e59eed01))
* **internal:** update conftest.py ([218e172](https://github.com/llamastack/llama-stack-client-python/commit/218e172c16014dad41a7c189c5620077955d6bdf))
* **readme:** update badges ([9b63e1b](https://github.com/llamastack/llama-stack-client-python/commit/9b63e1b7dbbbd7556d046a2a4224a8385bbea24c))
* **tests:** add tests for httpx client instantiation & proxies ([b27b11b](https://github.com/llamastack/llama-stack-client-python/commit/b27b11bbe0a9c5778b757733c11828d9603307ea))
* **tests:** run tests in parallel ([1287a3c](https://github.com/llamastack/llama-stack-client-python/commit/1287a3c11f668d916c8c7af534a48523e2e69140))
* **tests:** skip some failing tests on the latest python versions ([73b5705](https://github.com/llamastack/llama-stack-client-python/commit/73b57051c48d2ec42b844a288ffc9b5e3bbe6f2b))
* update SDK settings ([e54ba91](https://github.com/llamastack/llama-stack-client-python/commit/e54ba9163792ab80362a189acb825bcd00e5384b))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([497f2a1](https://github.com/llamastack/llama-stack-client-python/commit/497f2a198140f73525a880497bf1c51b5749c1f3))
