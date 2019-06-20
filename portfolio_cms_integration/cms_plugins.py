from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from portfolio_cms_integration.models import BlogPluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class BloginPublisher(CMSPluginBase):
    model = BlogPluginModel  # model where plugin data are saved
    module = _("Blogs")
    name = _("Blog Plugin")  # name of the plugin in the interface
    render_template = "portfolio_cms_integration/blog_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context