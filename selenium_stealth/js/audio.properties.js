(audio_properties = {}) => {
    function spoofAudioContextProperties(audio_properties) {
        const audioContextPrototype = AudioContext.prototype;

        // Spoof AudioContext properties
        Object.defineProperty(audioContextPrototype, 'sampleRate', {
            get: () => audio_properties.BaseAudioContextSampleRate || 48000
        });
        Object.defineProperty(audioContextPrototype, 'baseLatency', {
            get: () => audio_properties.AudioContextBaseLatency || 0.01
        });
        Object.defineProperty(audioContextPrototype, 'outputLatency', {
            get: () => audio_properties.AudioContextOutputLatency || 0
        });

        // Spoof AudioDestinationNode properties
        const originalDestination = audioContextPrototype.destination;
        Object.defineProperty(originalDestination, 'maxChannelCount', {
            get: () => audio_properties.AudioDestinationNodeMaxChannelCount || 2
        });

        // Spoof AnalyserNode properties
        const originalCreateAnalyser = audioContextPrototype.createAnalyser;
        audioContextPrototype.createAnalyser = function () {
            const analyser = originalCreateAnalyser.call(this);
            Object.defineProperty(analyser, 'fftSize', {
                get: () => audio_properties.AnalyzerNodeFftSize || 2048
            });
            Object.defineProperty(analyser, 'frequencyBinCount', {
                get: () => audio_properties.AnalyzerNodeFrequencyBinCount || 1024
            });
            Object.defineProperty(analyser, 'minDecibels', {
                get: () => audio_properties.AnalyzerNodeMinDecibels || -100
            });
            Object.defineProperty(analyser, 'maxDecibels', {
                get: () => audio_properties.AnalyzerNodeMaxDecibels || -30
            });
            Object.defineProperty(analyser, 'smoothingTimeConstant', {
                get: () => audio_properties.AnalyzerNodeSmoothingTimeConstant || 0.8
            });
            return analyser;
        };

        // Spoof BiquadFilterNode properties
        const originalCreateBiquadFilter = audioContextPrototype.createBiquadFilter;
        audioContextPrototype.createBiquadFilter = function () {
            const filter = originalCreateBiquadFilter.call(this);
            Object.defineProperty(filter, 'frequency', {
                get: () => ({
                    value: audio_properties.BiquadFilterNodeFrequencyDefaultValue || 350,
                    maxValue: audio_properties.BiquadFilterNodeFrequencyMaxValue || 24000,
                    minValue: audio_properties.BiquadFilterNodeFrequencyMinValue || 0
                })
            });
            Object.defineProperty(filter, 'detune', {
                get: () => ({
                    value: audio_properties.BiquadFilterNodeDetuneDefaultValue || 0,
                    maxValue: audio_properties.BiquadFilterNodeDetuneMaxValue || 153600,
                    minValue: audio_properties.BiquadFilterNodeDetuneMinValue || -153600
                })
            });
            Object.defineProperty(filter, 'Q', {
                get: () => ({
                    value: audio_properties.BiquadFilterNodeQDefaultValue || 1,
                    maxValue: audio_properties.BiquadFilterNodeQMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.BiquadFilterNodeQMinValue || -3.4028234663852886e+38
                })
            });
            Object.defineProperty(filter, 'gain', {
                get: () => ({
                    value: audio_properties.BiquadFilterNodeGainDefaultValue || 0,
                    maxValue: audio_properties.BiquadFilterNodeGainMaxValue || 1541.273681640625,
                    minValue: audio_properties.BiquadFilterNodeGainMinValue || -3.4028234663852886e+38
                })
            });
            Object.defineProperty(filter, 'type', {
                get: () => audio_properties.BiquadFilterNodeType || 'lowpass'
            });
            return filter;
        };

        // Spoof AudioBufferSourceNode properties
        const originalCreateBufferSource = audioContextPrototype.createBufferSource;
        audioContextPrototype.createBufferSource = function () {
            const source = originalCreateBufferSource.call(this);
            Object.defineProperty(source, 'detune', {
                get: () => ({
                    value: audio_properties.AudioBufferSourceNodeDetuneDefaultValue || 0,
                    maxValue: audio_properties.AudioBufferSourceNodeDetuneMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.AudioBufferSourceNodeDetuneMinValue || -3.4028234663852886e+38
                })
            });
            Object.defineProperty(source, 'playbackRate', {
                get: () => ({
                    value: audio_properties.AudioBufferSourceNodePlaybackRateDefaultValue || 1,
                    maxValue: audio_properties.AudioBufferSourceNodePlaybackRateMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.AudioBufferSourceNodePlaybackRateMinValue || -3.4028234663852886e+38
                })
            });
            return source;
        };

        // Spoof ConstantSourceNode properties
        const originalCreateConstantSource = audioContextPrototype.createConstantSource;
        audioContextPrototype.createConstantSource = function () {
            const source = originalCreateConstantSource.call(this);
            Object.defineProperty(source, 'offset', {
                get: () => ({
                    value: audio_properties.ConstantSourceNodeOffsetDefaultValue || 1,
                    maxValue: audio_properties.ConstantSourceNodeOffsetMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.ConstantSourceNodeOffsetMinValue || -3.4028234663852886e+38
                })
            });
            return source;
        };

        // Spoof DelayNode properties
        const originalCreateDelay = audioContextPrototype.createDelay;
        audioContextPrototype.createDelay = function () {
            const delay = originalCreateDelay.call(this);
            Object.defineProperty(delay, 'delayTime', {
                get: () => ({
                    value: audio_properties.DelayNodeDelayTimeDefaultValue || 0,
                    maxValue: audio_properties.DelayNodeDelayTimeMaxValue || 1,
                    minValue: audio_properties.DelayNodeDelayTimeMinValue || 0
                })
            });
            return delay;
        };

        // Spoof DynamicsCompressorNode properties
        const originalCreateDynamicsCompressor = audioContextPrototype.createDynamicsCompressor;
        audioContextPrototype.createDynamicsCompressor = function () {
            const compressor = originalCreateDynamicsCompressor.call(this);
            Object.defineProperty(compressor, 'threshold', {
                get: () => ({
                    value: audio_properties.DynamicsCompressorNodeThresholdDefaultValue || -24,
                    maxValue: audio_properties.DynamicsCompressorNodeThresholdMaxValue || 0,
                    minValue: audio_properties.DynamicsCompressorNodeThresholdMinValue || -100
                })
            });
            Object.defineProperty(compressor, 'knee', {
                get: () => ({
                    value: audio_properties.DynamicsCompressorNodeKneeDefaultValue || 30,
                    maxValue: audio_properties.DynamicsCompressorNodeKneeMaxValue || 40,
                    minValue: audio_properties.DynamicsCompressorNodeKneeMinValue || 0
                })
            });
            Object.defineProperty(compressor, 'ratio', {
                get: () => ({
                    value: audio_properties.DynamicsCompressorNodeRatioDefaultValue || 12,
                    maxValue: audio_properties.DynamicsCompressorNodeRatioMaxValue || 20,
                    minValue: audio_properties.DynamicsCompressorNodeRatioMinValue || 1
                })
            });
            Object.defineProperty(compressor, 'attack', {
                get: () => ({
                    value: audio_properties.DynamicsCompressorNodeAttackDefaultValue || 0.003,
                    maxValue: audio_properties.DynamicsCompressorNodeAttackMaxValue || 1,
                    minValue: audio_properties.DynamicsCompressorNodeAttackMinValue || 0
                })
            });
            Object.defineProperty(compressor, 'release', {
                get: () => ({
                    value: audio_properties.DynamicsCompressorNodeReleaseDefaultValue || 0.25,
                    maxValue: audio_properties.DynamicsCompressorNodeReleaseMaxValue || 1,
                    minValue: audio_properties.DynamicsCompressorNodeReleaseMinValue || 0
                })
            });
            Object.defineProperty(compressor, 'reduction', {
                get: () => audio_properties.DynamicsCompressorNodeReduction || 0
            });
            return compressor;
        };

        // Spoof GainNode properties
        const originalCreateGain = audioContextPrototype.createGain;
        audioContextPrototype.createGain = function () {
            const gain = originalCreateGain.call(this);
            Object.defineProperty(gain, 'gain', {
                get: () => ({
                    value: audio_properties.GainNodeGainDefaultValue || 1,
                    maxValue: audio_properties.GainNodeGainMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.GainNodeGainMinValue || -3.4028234663852886e+38
                })
            });
            return gain;
        };

        // Spoof OscillatorNode properties
        const originalCreateOscillator = audioContextPrototype.createOscillator;
        audioContextPrototype.createOscillator = function () {
            const oscillator = originalCreateOscillator.call(this);
            Object.defineProperty(oscillator, 'frequency', {
                get: () => ({
                    value: audio_properties.OscillatorNodeFrequencyDefaultValue || 440,
                    maxValue: audio_properties.OscillatorNodeFrequencyMaxValue || 24000,
                    minValue: audio_properties.OscillatorNodeFrequencyMinValue || -24000
                })
            });
            Object.defineProperty(oscillator, 'detune', {
                get: () => ({
                    value: audio_properties.OscillatorNodeDetuneDefaultValue || 0,
                    maxValue: audio_properties.OscillatorNodeDetuneMaxValue || 153600,
                    minValue: audio_properties.OscillatorNodeDetuneMinValue || -153600
                })
            });
            Object.defineProperty(oscillator, 'type', {
                get: () => audio_properties.OscillatorNodeType || 'sine'
            });
            return oscillator;
        };

        // Spoof StereoPannerNode properties
        const originalCreateStereoPanner = audioContextPrototype.createStereoPanner;
        audioContextPrototype.createStereoPanner = function () {
            const panner = originalCreateStereoPanner.call(this);
            Object.defineProperty(panner, 'pan', {
                get: () => ({
                    value: audio_properties.StereoPannerNodePanDefaultValue || 0,
                    maxValue: audio_properties.StereoPannerNodePanMaxValue || 1,
                    minValue: audio_properties.StereoPannerNodePanMinValue || -1
                })
            });
            return panner;
        };

        // Spoof AudioListener properties
        const originalListener = audioContextPrototype.listener;
        Object.defineProperty(originalListener, 'positionX', {
            get: () => ({
                value: audio_properties.AudioListenerPositionXDefaultValue || 0,
                maxValue: audio_properties.AudioListenerPositionXMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerPositionXMinValue || -3.4028234663852886e+38
            })
        });
        Object.defineProperty(originalListener, 'positionY', {
            get: () => ({
                value: audio_properties.AudioListenerPositionYDefaultValue || 0,
                maxValue: audio_properties.AudioListenerPositionYMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerPositionYMinValue || -3.4028234663852886e+38
            })
        });
        Object.defineProperty(originalListener, 'positionZ', {
            get: () => ({
                value: audio_properties.AudioListenerPositionZDefaultValue || 0,
                maxValue: audio_properties.AudioListenerPositionZMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerPositionZMinValue || -3.4028234663852886e+38
            })
        });
        Object.defineProperty(originalListener, 'forwardX', {
            get: () => ({
                value: audio_properties.AudioListenerForwardXDefaultValue || 0,
                maxValue: audio_properties.AudioListenerForwardXMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerForwardXMinValue || -3.4028234663852886e+38
            })
        });
        Object.defineProperty(originalListener, 'forwardY', {
            get: () => ({
                value: audio_properties.AudioListenerForwardYDefaultValue || 0,
                maxValue: audio_properties.AudioListenerForwardYMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerForwardYMinValue || -3.4028234663852886e+38
            })
        });
        Object.defineProperty(originalListener, 'forwardZ', {
            get: () => ({
                value: audio_properties.AudioListenerForwardZDefaultValue || -1,
                maxValue: audio_properties.AudioListenerForwardZMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerForwardZMinValue || -3.4028234663852886e+38
            })
        });
        Object.defineProperty(originalListener, 'upX', {
            get: () => ({
                value: audio_properties.AudioListenerUpXDefaultValue || 0,
                maxValue: audio_properties.AudioListenerUpXMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerUpXMinValue || -3.4028234663852886e+38
            })
        });
        Object.defineProperty(originalListener, 'upY', {
            get: () => ({
                value: audio_properties.AudioListenerUpYDefaultValue || 1,
                maxValue: audio_properties.AudioListenerUpYMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerUpYMinValue || -3.4028234663852886e+38
            })
        });
        Object.defineProperty(originalListener, 'upZ', {
            get: () => ({
                value: audio_properties.AudioListenerUpZDefaultValue || 0,
                maxValue: audio_properties.AudioListenerUpZMaxValue || 3.4028234663852886e+38,
                minValue: audio_properties.AudioListenerUpZMinValue || -3.4028234663852886e+38
            })
        });

        // Spoof PannerNode properties
        const originalCreatePanner = audioContextPrototype.createPanner;
        audioContextPrototype.createPanner = function () {
            const panner = originalCreatePanner.call(this);
            Object.defineProperty(panner, 'positionX', {
                get: () => ({
                    value: audio_properties.PannerNodePositionXDefaultValue || 0,
                    maxValue: audio_properties.PannerNodePositionXMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.PannerNodePositionXMinValue || -3.4028234663852886e+38
                })
            });
            Object.defineProperty(panner, 'positionY', {
                get: () => ({
                    value: audio_properties.PannerNodePositionYDefaultValue || 0,
                    maxValue: audio_properties.PannerNodePositionYMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.PannerNodePositionYMinValue || -3.4028234663852886e+38
                })
            });
            Object.defineProperty(panner, 'positionZ', {
                get: () => ({
                    value: audio_properties.PannerNodePositionZDefaultValue || 0,
                    maxValue: audio_properties.PannerNodePositionZMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.PannerNodePositionZMinValue || -3.4028234663852886e+38
                })
            });
            Object.defineProperty(panner, 'orientationX', {
                get: () => ({
                    value: audio_properties.PannerNodeOrientationXDefaultValue || 1,
                    maxValue: audio_properties.PannerNodeOrientationXMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.PannerNodeOrientationXMinValue || -3.4028234663852886e+38
                })
            });
            Object.defineProperty(panner, 'orientationY', {
                get: () => ({
                    value: audio_properties.PannerNodeOrientationYDefaultValue || 0,
                    maxValue: audio_properties.PannerNodeOrientationYMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.PannerNodeOrientationYMinValue || -3.4028234663852886e+38
                })
            });
            Object.defineProperty(panner, 'orientationZ', {
                get: () => ({
                    value: audio_properties.PannerNodeOrientationZDefaultValue || 0,
                    maxValue: audio_properties.PannerNodeOrientationZMaxValue || 3.4028234663852886e+38,
                    minValue: audio_properties.PannerNodeOrientationZMinValue || -3.4028234663852886e+38
                })
            });
            return panner;
        };
    }
    return spoofAudioContextProperties(audio_properties);
}