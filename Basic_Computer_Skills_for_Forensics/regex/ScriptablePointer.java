/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.cocoon.components.flow.javascript;

import java.util.Locale;

import org.apache.commons.jxpath.ri.QName;
import org.apache.commons.jxpath.ri.model.NodePointer;
import org.apache.commons.jxpath.ri.model.beans.PropertyPointer;
import org.apache.commons.jxpath.ri.model.dynamic.DynamicPointer;
import org.mozilla.javascript.NativeArray;
import org.mozilla.javascript.Scriptable;
import org.mozilla.javascript.ScriptableObject;
import org.mozilla.javascript.Wrapper;

/**
 *
 * @version CVS $Id: ScriptablePointer.java 433543 2006-08-22 06:22:54Z crossley $
 */
public class ScriptablePointer extends DynamicPointer {

    Scriptable node;

    final static ScriptablePropertyHandler handler = 
        new ScriptablePropertyHandler();

    public ScriptablePointer(NodePointer parent,
                             QName name,
                             Scriptable object) {
        super(parent, name, object, handler);
        node = object;
    }

    public ScriptablePointer(QName name,
                             Scriptable object,
                             Locale locale) {
        super(name, object, handler, locale);
        node = object;
    }

    public PropertyPointer getPropertyPointer(){
        return new ScriptablePropertyPointer(this, handler);
    }

    public int getLength() {
        Object obj = getBaseValue();
        if (obj instanceof Scriptable) {
            Scriptable node = (Scriptable)obj;
            if (node instanceof NativeArray) {
                return (int)((NativeArray)node).jsGet_length();
            }
            if (ScriptableObject.hasProperty(node, "length")) {
                Object val = ScriptableObject.getProperty(node, "length");
                if (val instanceof Number) {
                    return ((Number)val).intValue();
                }
            }
        }
        return super.getLength();
    }

    public Object getImmediateNode() {
        Object value;
        if (index == WHOLE_COLLECTION) {
            value = node;
        } else {
            value = ScriptableObject.getProperty(node, index);
            if (value == Scriptable.NOT_FOUND) {
                value = node; // hack: same behavior as ValueUtils.getValue()
            } 
        }
        if (value instanceof Wrapper) {
            value = ((Wrapper)value).unwrap();
        }
        return value;
    }

    public void setValue(Object value){
        if (getParent() != null) {
            getParent().setValue(value);
        }
    }

}
