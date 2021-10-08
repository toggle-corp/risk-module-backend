"""Plugin loader"""

import importlib
import logging

LOGGER = logging.getLogger(__name__)

#: Loads provider plugins to be used by pygeoapi,\
#: formatters and processes available
PLUGINS = {
    'provider': {
        'CSV': 'pygeoapi.provider.csv_.CSVProvider',
        'Elasticsearch': 'pygeoapi.provider.elasticsearch_.ElasticsearchProvider',  # noqa
        'ElasticsearchCatalogue': 'pygeoapi.provider.elasticsearch_.ElasticsearchCatalogueProvider',  # noqa
        'GeoJSON': 'pygeoapi.provider.geojson.GeoJSONProvider',
        'OGR': 'pygeoapi.provider.ogr.OGRProvider',
        'PostgreSQL': 'pygeoapi.provider.postgresql.PostgreSQLProvider',
        'SQLiteGPKG': 'pygeoapi.provider.sqlite.SQLiteGPKGProvider',
        'MongoDB': 'pygeoapi.provider.mongo.MongoProvider',
        'FileSystem': 'pygeoapi.provider.filesystem.FileSystemProvider',
        'rasterio': 'pygeoapi.provider.rasterio_.RasterioProvider',
        'xarray': 'pygeoapi.provider.xarray_.XarrayProvider',
        'MVT': 'pygeoapi.provider.mvt.MVTProvider',
        'TinyDBCatalogue': 'pygeoapi.provider.tinydb_.TinyDBCatalogueProvider',
        'SensorThings': 'pygeoapi.provider.sensorthings.SensorThingsProvider',
        'xarray-edr': 'pygeoapi.provider.xarray_edr.XarrayEDRProvideri',
        'earthquake': 'pygeoapi.provider.earthquake_rasterio_.EarthquakeRasterioProvider',
    },
    'formatter': {
        'CSV': 'pygeoapi.formatter.csv_.CSVFormatter'
    },
    'process': {
        'HelloWorld': 'pygeoapi.process.hello_world.HelloWorldProcessor'
    },
    'process_manager': {
        'Dummy': 'pygeoapi.process.manager.dummy.DummyManager',
        'TinyDB': 'pygeoapi.process.manager.tinydb_.TinyDBManager'
    }
}


def load_plugin(plugin_type, plugin_def):
    """
    loads plugin by name
    :param plugin_type: type of plugin (provider, formatter)
    :param plugin_def: plugin definition
    :returns: plugin object
    """

    name = plugin_def['name']

    if plugin_type not in PLUGINS.keys():
        msg = 'Plugin type {} not found'.format(plugin_type)
        LOGGER.exception(msg)
        raise InvalidPluginError(msg)

    plugin_list = PLUGINS[plugin_type]

    LOGGER.debug('Plugins: {}'.format(plugin_list))

    if '.' not in name and name not in plugin_list.keys():
        msg = 'Plugin {} not found'.format(name)
        LOGGER.exception(msg)
        raise InvalidPluginError(msg)

    if '.' in name:  # dotted path
        packagename, classname = name.rsplit('.', 1)
    else:  # core formatter
        packagename, classname = plugin_list[name].rsplit('.', 1)

    LOGGER.debug('package name: {}'.format(packagename))
    LOGGER.debug('class name: {}'.format(classname))

    module = importlib.import_module(packagename)
    class_ = getattr(module, classname)
    plugin = class_(plugin_def)

    return plugin


class InvalidPluginError(Exception):
    """Invalid plugin"""
    pass
