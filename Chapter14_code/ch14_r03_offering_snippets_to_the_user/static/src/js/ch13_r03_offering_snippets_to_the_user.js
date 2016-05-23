odoo.define('ch14_r03_offering_snippets_to_the_user.snippets_animation', function(require)
{
    "use strict";
    var animation = require('web_editor.snippets.animation'),
        Model = require('web.Model');

    animation.registry.book_snippet = animation.Class.extend({
        selector: ".book_snippet",
        start: function()
        {
            var self = this,
                number = 3;
            _.each(this.$el.attr('class').split(/\s+/), function(cls)
            {
                if(cls.indexOf('book_snippet-show') == 0)
                {
                    number = parseInt(cls.substring('book_snippet-show'.length));
                }
            });
            this.$el.find('td').parents('tr').remove();
            new Model('library.book')
            .call(
                'search_read', [],
                {
                    domain: [],
                    fields: ['name', 'date_release'],
                    order: 'date_release desc',
                    limit: number,
                })
            .then(function(data)
            {
                var $table = self.$el.find('table');
                _.each(data, function(book)
                {
                    $table.append(
                        jQuery('<tr />')
                        .append(
                            jQuery('<td />').text(book.name),
                            jQuery('<td />').text(book.date_release)
                        )
                    );
                })
            });
        },
    });

});
